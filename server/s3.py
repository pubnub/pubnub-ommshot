import base64
import hmac
import os
import sha
from hashlib import sha1
import time
import tornado

def upload(
    access_key,
    secret_key,
    bucket,
    key,
    data='Empty',
    headers={},
    callback=None
):
    tornado.httpclient.AsyncHTTPClient().fetch(
        'http://%s.s3.amazonaws.com/%s' % ( bucket, key ),
        method='PUT',
        body=data,
        callback=callback,
        connect_timeout=10,
        request_timeout=10,
        headers=_get_auth_header(
            access_key,
            secret_key,
            'PUT',
            bucket,
            key,
            headers=headers
        )
    )

def _get_auth_header(
    access_key,
    secret_key,
    method,
    bucket,
    key,
    headers={}
):
    # Add the date to the amz headers.
    date = time.strftime("%a, %d %b %Y %X GMT", time.gmtime())

    # Create String to Sign
    sign_string = "\n".join([
        "{method}\n",
        "{content}",
        "{date}",
        "x-amz-acl:{acl}",
        "/{bucket}/{key}"
    ]).format(
        method=method,
        acl=headers['x-amz-acl'],
        content=headers['Content-Type'],
        date=date,
        bucket=bucket,
        key=key
    )

    auth_string = base64.encodestring(hmac.new(
        secret_key,
        sign_string,
        sha1
    ).digest()).strip()

    headers['Date']           = date
    headers['Authorization']  = 'AWS %s:%s' % (access_key, auth_string)

    return headers

