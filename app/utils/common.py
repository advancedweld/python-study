# 公共 response 方法
def res_common(data=None, message='Ok', success=True, code=200):
  return {
    'success': success,
    'message': message,
    'data': data,
   }, code
