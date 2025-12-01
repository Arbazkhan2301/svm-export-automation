from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
import os

SHAREPOINT_SITE_URL = "https://innomotics.sharepoint.com/sites/ProductandSolutionSecurity/_layouts/15/viewlsts.aspx?view=14"
DOC_LIBRARY = "Documents"

SHAREPOINT_SITE = os.environ.get("https://innomotics.sharepoint.com/sites/ProductandSolutionSecurity/_layouts/15/viewlsts.aspx?view=14")
SHAREPOINT_USERNAME = os.environ.get("khan.arbaz@innomotics.com")
SHAREPOINT_PASSWORD = os.environ.get("Ilyas12345$@")
SHAREPOINT_FOLDER = os.environ.get("Documents")

ctx = ClientContext(SHAREPOINT_SITE_URL).with_credentials(
    ClientCredential(CLIENT_ID, CLIENT_SECRET)
)

def upload_file(local_path, target_folder=None):
    filename = os.path.basename(local_path)

    if target_folder:
        target_folder = f"{DOC_LIBRARY}/{target_folder}"
    else:
        folder_url = DOC_LIBRARY

    folder = ctx.web.get_folder_by_server_relative_url(folder_url)
    with open(local_path, "rb") as content_file:
        folder.upload_file(filename, content_file).execute_query()

    print(f"Uploaded {filename} to SharePoint folder {folder_url} successfully!")

