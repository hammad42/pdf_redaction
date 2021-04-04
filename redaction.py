def redact_(file_name,project):
    import re
    
    output_file_name=re.split('[.]',file_name)
    output_file_name=output_file_name[0]+'_redacted'+'.'+output_file_name[1]
    import mimetypes
    import google.cloud.dlp
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\gcp_credentials\elaborate-howl-285701-105c2e8355a8.json"
    dlp = google.cloud.dlp_v2.DlpServiceClient()
    info_types=['EMAIL_ADDRESS','PHONE_NUMBER']#info types need to redacted
    info_types = [{"name": info_type} for info_type in info_types]
    
    image_redaction_configs = []#redaction config
    inspect_config = { #inspection config
        "min_likelihood": 'POSSIBLE',
        "info_types": info_types,
    }
    #filename='page0.jpg'
    #project='elaborate-howl-285701'
    if info_types is not None:
        for info_type in info_types:
            image_redaction_configs.append({"info_type": info_type})
    supported_content_types = {
        None: 0,  # "Unspecified"
        "image/jpeg": 1,
        "image/bmp": 2,
        "image/png": 3,
        "image/svg": 4,
        "text/plain": 5,
    
    }
    content_type_index = supported_content_types.get("application/octet-stream",1)
    with open(file_name, mode="rb") as f:
        byte_item = {"type_": content_type_index, "data": f.read()}
    parent = f"projects/{project}"
    response = dlp.redact_image(
        request={
            "parent": parent,
            "inspect_config": inspect_config,
            "image_redaction_configs": image_redaction_configs,
            "byte_item": byte_item,
        }
    )
    with open(output_file_name, mode="wb") as f:
        f.write(response.redacted_image)
    print(
        "Wrote {byte_count} to {filename}".format(
            byte_count=len(response.redacted_image), filename=output_file_name
        )
    )
    return(output_file_name)