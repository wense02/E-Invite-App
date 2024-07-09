from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os

def generate_invitation_card(name, invite_link):
    # Load the designed card from the media folder
    designed_card_path = os.path.join(settings.MEDIA_ROOT, 'Qavah_generated.png')
    card = Image.open(designed_card_path)

    # Generate QR code for the invite link
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(invite_link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')
    
    # Resize the QR code if necessary
    qr_img = qr_img.resize((200, 200), Image.Resampling.LANCZOS)  # Adjust size as needed
    
    # Paste the QR code onto the Canva-designed card
    position_x, position_y = 200, 150  # Adjust position as needed
    card.paste(qr_img, (position_x, position_y))
    
    # Save the card to the media directory
    media_path = settings.MEDIA_ROOT
    if not os.path.exists(media_path):
        os.makedirs(media_path)
    card_filename = f'invitation_{name}.png'
    card_filepath = os.path.join(media_path, card_filename)
    card.save(card_filepath)
    
    return card_filepath, card_filename

def send_invite_email(name, email, invite_link):
    card_filepath, card_filename = generate_invitation_card(name, invite_link)
    
    subject = 'You are invited!'
    text_content = f'Hello {name},\n\nYou have been invited. Please join us!'
    html_content = f"""
    <html>
        <body>
            <p>Hello {name},</p>
            <p>You have been invited. Please join us by clicking the link below:</p>
            <p><a href="{invite_link}">Accept Invite</a></p>
        </body>
    </html>
    """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]

    msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    
    # Attach the image file
    with open(card_filepath, 'rb') as card_file:
        msg.attach(card_filename, card_file.read(), 'image/png')
    
    msg.send()
