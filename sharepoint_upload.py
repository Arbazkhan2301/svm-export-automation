from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
import os

# SHAREPOINT_SITE_URL = "https://innomotics.sharepoint.com/sites/ProductandSolutionSecurity/_layouts/15/viewlsts.aspx?view=14"
# DOC_LIBRARY = "Documents"

SHAREPOINT_SITE = os.environ.get("SHAREPOINT_SITE")
SHAREPOINT_USERNAME = os.environ.get("SHAREPOINT_USERNAME")
SHAREPOINT_PASSWORD = os.environ.get("SHAREPOINT_PASSWORD")
SHAREPOINT_FOLDER = os.environ.get("SHAREPOINT_FOLDER", "Documents")

ctx = ClientContext(SHAREPOINT_SITE).with_credentials(
    ClientCredential(SHAREPOINT_USERNAME, SHAREPOINT_PASSWORD)
)

# def upload_file(local_path, target_folder=None):
#     filename = os.path.basename(local_path)
#     folder_url = target_folder if target_folder else SHAREPOINT_FOLDER

#     folder = ctx.web.get_folder_by_server_relative_url(folder_url)
#     with open(local_path, "rb") as content_file:
#         folder.upload_file(filename, content_file).execute_query()

#     print(f"Uploaded {filename} to SharePoint folder {folder_url} successfully!")

    
def upload_file(local_path, target_folder=None):
    from os.path import basename
    filename = basename(local_path)
    folder_url = target_folder if target_folder else SHAREPOINT_FOLDER

    print(f"Attempting to upload {filename} to SharePoint folder: {folder_url}")
    print(f"Using site: {SHAREPOINT_SITE}")
    print(f"Using username: {SHAREPOINT_USERNAME}")

    try:
        folder = ctx.web.get_folder_by_server_relative_url(folder_url)
        with open(local_path, "rb") as content_file:
            folder.upload_file(filename, content_file.read()).execute_query()
        print(f"Uploaded {filename} to SharePoint folder {folder_url} successfully!")
    except Exception as e:
        print(f"ERROR uploading {filename}: {e}")

