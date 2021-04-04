def dlp_redation(request):
    request_json = request.get_json()
    if request_json:

        source_url = request_json['source_url']
        print("source_url="+source_url)
    from sep_blob_bucket import regex_#module for seperating bucket name and blob name from cloud storage bucket
    from storage_download import download_blob
    import re
    import os
    from pdf2image import convert_from_path, convert_from_bytes
    from redaction import redact_
    from image2pdf import pdf_conv
    import PyPDF2
    pdfWriter=PyPDF2.PdfFileWriter()


    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\gcp_credentials\elaborate-howl-285701-105c2e8355a8.json"
    link=regex_(source_url)#"gs://context_primary/Forms/NotProcessed/DD2875_AUG_2009_wh (1).pdf"
    #print(link) #link name
    bucket_and_blob=re.split('[+]',link)
    bucket_name=bucket_and_blob[0]#bucket name in gcs
    blob_name=bucket_and_blob[1]#blob name in gcs
    print(bucket_name)
    print(blob_name)

    pdf_as_bytes=download_blob(bucket_name,blob_name).download_as_bytes()#downloading pdf as bytes
    #print(pdf_as_bytes)
    images = convert_from_bytes(pdf_as_bytes)
    for x in range(0,len(images)):
        output_file_name="page"+str(x)+'.jpg'
        converted_pdf2image=images[x].save(output_file_name,'JPEG')#saving pdfs in directory
        #pdf_conv(redact_(output_file_name,'elaborate-howl-285701'))
        pdf1File=open(pdf_conv(redact_(output_file_name,'elaborate-howl-285701')),'rb') 
        pdf1Reader=PyPDF2.PdfFileReader(pdf1File)
        for pageNum in range(pdf1Reader.numPages):
            pageObj = pdf1Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    pdfOutputFile = open('MergedFiles.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    return("success")







