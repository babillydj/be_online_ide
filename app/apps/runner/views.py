import sys

import io
from contextlib import redirect_stdout

# import epicbox

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from core.base import BaseResponse


@api_view(['POST'])
@permission_classes([AllowAny, ])
def run_code(request):
    code = request.data.get('code')
    with io.StringIO() as f:
        with redirect_stdout(f):
            try:
                exec(code)
                output = f.getvalue()
            except Exception as e:
                print(e)
                output = f.getvalue() + str(e)
    res = {"output": output}
    return BaseResponse(res, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def run_code2(request):
    code = request.data.get('code')
    try:
        sys.stdout = open('file.txt', 'w')
        exec(code)
        sys.stdout.close()
        output = open('file.txt', 'r').read()
    except Exception as e:
        sys.stdout.close()
        output = open('file.txt', 'r').read() + str(e)
    res = {"output": output}
    return BaseResponse(res, status=status.HTTP_200_OK)


# @api_view(['POST'])
# @permission_classes([AllowAny, ])
# def run_code3(request):
#     code = request.data.get('code')
#     epicbox.configure(
#         profiles=[
#             epicbox.Profile('python', 'python:3.6.5-alpine')
#         ]
#     )
#     files = [{'name': 'main.py', 'content': b'print(42)'}]
#     limits = {'cputime': 1, 'memory': 64}
#     result = epicbox.run('python', 'python3 main.py', files=files, limits=limits)
#     print(result)
#     return BaseResponse(result, status=status.HTTP_200_OK)
