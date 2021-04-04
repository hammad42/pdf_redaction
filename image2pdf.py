def pdf_conv(img_path):
    import img2pdf
    from PIL import Image
    import os
    import re
    #img_path = "page0_redacted.jpg"
    pdf_path=re.sub(".jpg",'.pdf',img_path)
    image = Image.open(img_path)
    pdf_bytes = img2pdf.convert(image.filename)
    file = open(pdf_path, "wb")
    file.write(pdf_bytes)
    image.close()
    file.close()
    return(pdf_path)