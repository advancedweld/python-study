import os
from flask import request, current_app
from flask_restful import Resource
from werkzeug.utils import secure_filename
from datetime import datetime
# 允许的文件扩展名
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx', 'xls', 'docx', 'edf', 'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class FileUpload(Resource):
    def post(self):
        # 上传目录从Flask配置中读取
        upload_folder = current_app.config.get('UPLOAD_FOLDER')
        if not upload_folder:
            return {
                'success': False,
                'message': 'Upload folder is not configured',
                'data': None,
            }, 500

        # 确保上传目录存在
        os.makedirs(upload_folder, exist_ok=True)
        user_token = request.form.get('user_token')
        print('@@@ user_token:',user_token)
        print('@@@ request.files:',request.files)
        if 'file' not in request.files:
            return {
                'success': False,
                'message': 'No file part in the request',
                'data': None,
            }, 400

# 这里file是一个FileStorage 对象
        file = request.files['file']
        if file.filename == '':
            return {
                'success': False,
                'message': 'No selected file',
                'data': None,
            }, 400

        if file and allowed_file(file.filename):
            print('@@@ file is ok:',file)
            filename = secure_filename(file.filename)

                # 获取当前时间戳
            timestamp = datetime.now().strftime("%Y%m%d_%H_%M_%S")
            # 在文件名中插入时间戳
            base, extension = os.path.splitext(filename)
            filename_with_timestamp = f"{base}_{timestamp}{extension}"
            try:
                file.save(os.path.join(upload_folder, filename_with_timestamp))
                return {
                    'success': True,
                    'message': 'File uploaded successfully',
                    'data': {'filename': filename},
                }, 200
            except Exception as e:
                print('@@@ upload error:',e)
                return {
                    'success': False,
                    'message': f'Error saving file: {e}',
                    'data': None,
                }, 500
        else:
            return {
                'success': False,
                'message': 'File type not allowed',
                'data': None,
            }, 400
