import gdown

def download_from_gdrive(file_id, output_path):
    # Construct the Google Drive download URL
    url = f'https://drive.google.com/uc?id={file_id}'

    # Download the file
    gdown.download(url, output_path, quiet=False)

if __name__ == '__main__':
    download_from_gdrive('1Tw5QHriicl-8ITkLeTgHP3yarTqGJ4Au', './')

#https://drive.google.com/file/d/1Tw5QHriicl-8ITkLeTgHP3yarTqGJ4Au/view?usp=sharing