        to_addresses = {'toRecipients': []}
        cc_addresses = {'ccRecipients': []}
        bcc_addresses = {'bccRecipients': []}

        if 'to' in req_data['templateParams']:
            to_data = req_data['templateParams']['to']

            # PARSE DATA ACCORDINGLY

            # to_addresses = {'toRecipients': []}

            # List comprehension to delete space into the list
            to_data_list = [x.replace(' ', '') for x in to_data]

            for email in to_data_list:
                if is_valid_email(email):
                    to_addresses['toRecipients'].append(
                        {'emailAddress': {'address': email}}
                    )

                else:
                    resp_data['errors'].append('email {} is not valid. Did not add.'.format(email))

                if not to_addresses['toRecipients']:
                    resp_data['errors'].append('No email addresses received. Cannot send email.')
                    return json.dumps(resp_data), 500, headers

        if 'cc' in req_data['templateParams']:
            cc_data = req_data['templateParams']['cc']

            # cc_addresses = {'ccRecipients': []}

            # List comprehension to delete space into the list
            cc_data_list = [x.replace(' ', '') for x in cc_data]

            for email in cc_data_list:
                if is_valid_email(email):
                    cc_addresses['ccRecipients'].append(
                        {'emailAddress': {'address': email}}
                    )

                else:
                    resp_data['errors'].append('email {} is not valid. Did not add.'.format(email))

                if not cc_addresses['ccRecipients']:
                    resp_data['errors'].append('No email addresses received. Cannot send email.')
                    return json.dumps(resp_data), 500, headers



        if 'bcc' in req_data['templateParams']:
            bcc_data = req_data['templateParams']['bcc']

            # bcc_addresses = {'bccRecipients': []}

            # List comprehension to delete space into the list
            bcc_data_list = [x.replace(' ', '') for x in bcc_data]

            for email in bcc_data_list:
                if is_valid_email(email):
                    bcc_addresses['bccRecipients'].append(
                        {'emailAddress': {'address': email}}
                    )

                else:
                    resp_data['errors'].append('email {} is not valid. Did not add.'.format(email))

                if not bcc_addresses['bccRecipients']:
                    resp_data['errors'].append('No email addresses received. Cannot send email.')
                    return json.dumps(resp_data), 500, headers



        #   Any errors?
        if len(resp_data['errors']) > 0:
            resp_data['status'] = 'error'
            return json.dumps(resp_data), 404, headers

        try:

            # Getting access token
            base_url = "https://login.microsoftonline.com/36eae5cd-e5ad-4ea6-9d47-86fca48c4841/oauth2/token"
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}

            dict_get_token =  {'username': app.config.get('USERNAME'),
                               'password': app.config.get('PASSWORD'),
                               'grant_type': app.config.get('GRANT_TYPE'),
                               'resource': app.config.get('RESOURCE'),
                               'client_id': app.config.get('CLIENT_ID'),
                               'client_secret': app.config.get('CLIENT_SECRET')
                              }

            resp_data = {'status': 'fail', 'errors': []}

            r = requests.post(base_url, data=dict_get_token, headers=headers)
            get_r = r.json()

            if r.status_code != 200:
                resp_data['errors'].append('No auth token returned.')
                return json.dumps(resp_data), 500, headers

            else:
                access_token = get_r['access_token']
                auth = 'Bearer ' + access_token
                from_address = req_data['templateParams']['from']

                base_url = "https://graph.microsoft.com/v1.0/users/" + from_address + "/sendMail"
                headers = {'Content-Type': 'application/json', 'Authorization': auth}

                subject = req_data['templateParams']['subject']
                body = req_data['templateParams']['body']

                payload = {
                    "message": {
                        "subject": subject,
                        "body": {
                            "contentType": "Text",
                            "content": body
                        },
                        "toRecipients": to_addresses['toRecipients'],
                        "ccRecipients": cc_addresses['ccRecipients'],
                        "bccRecipients": bcc_addresses['bccRecipients']
                    },
                    "saveToSentItems": "false"
                }
                r = requests.post(base_url, json=payload, headers=headers)
                if r.status_code != 202:
                    resp_data['errors'].append('Cannot send email.')
                    return json.dumps(resp_data), 500, headers
                else:
                    resp_data['status'] = 'success'
                    resp_data['data'] = None
                    return json.dumps(resp_data), 200, headers

        # return json.dumps(payload)
        except Exception as e:
            resp_data['errors'].append('Cannot send email')
            return json.dumps(resp_data), 500, headers




#------------------------------ Another script, v2 

        if template_name == 'gis.service.degradation':

            if 'to' in req_data['templateParams']:
                to_data = req_data['templateParams']['to']

                # PARSE DATA ACCORDINGLY

                # to_addresses = {'toRecipients': []}

                # List comprehension to delete space into the list
                to_data_list = [x.replace(' ', '') for x in to_data]

                for email in to_data_list:
                    if is_valid_email(email):
                        to_addresses['toRecipients'].append(
                            {'emailAddress': {'address': email}}
                        )

                    else:
                        resp_data['errors'].append('email {} is not valid. Did not add.'.format(email))

                    if not to_addresses['toRecipients']:
                        resp_data['errors'].append('No email addresses received. Cannot send email.')
                        return json.dumps(resp_data), 500, headers

            if 'cc' in req_data['templateParams']:
                cc_data = req_data['templateParams']['cc']

                # cc_addresses = {'ccRecipients': []}

                # List comprehension to delete space into the list
                cc_data_list = [x.replace(' ', '') for x in cc_data]

                for email in cc_data_list:
                    if is_valid_email(email):
                        cc_addresses['ccRecipients'].append(
                            {'emailAddress': {'address': email}}
                        )

                    else:
                        resp_data['errors'].append('email {} is not valid. Did not add.'.format(email))

                    if not cc_addresses['ccRecipients']:
                        resp_data['errors'].append('No email addresses received. Cannot send email.')
                        return json.dumps(resp_data), 500, headers

            if 'bcc' in req_data['templateParams']:
                bcc_data = req_data['templateParams']['bcc']

                # bcc_addresses = {'bccRecipients': []}

                # List comprehension to delete space into the list
                bcc_data_list = [x.replace(' ', '') for x in bcc_data]

                for email in bcc_data_list:
                    if is_valid_email(email):
                        bcc_addresses['bccRecipients'].append(
                            {'emailAddress': {'address': email}}
                        )

                    else:
                        resp_data['errors'].append('email {} is not valid. Did not add.'.format(email))

                    if not bcc_addresses['bccRecipients']:
                        resp_data['errors'].append('No email addresses received. Cannot send email.')
                        return json.dumps(resp_data), 500, headers

            #   Any errors?
            if len(resp_data['errors']) > 0:
                resp_data['status'] = 'error'
                return json.dumps(resp_data), 404, headers

            try:

                # Getting access token
                base_url = "https://login.microsoftonline.com/36eae5cd-e5ad-4ea6-9d47-86fca48c4841/oauth2/token"
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}

                dict_get_token = {'username': app.config.get('USERNAME'),
                                  'password': app.config.get('PASSWORD'),
                                  'grant_type': app.config.get('GRANT_TYPE'),
                                  'resource': app.config.get('RESOURCE'),
                                  'client_id': app.config.get('CLIENT_ID'),
                                  'client_secret': app.config.get('CLIENT_SECRET')
                                  }

                resp_data = {'status': 'fail', 'errors': []}

                r = requests.post(base_url, data=dict_get_token, headers=headers)
                get_r = r.json()

                if r.status_code != 200:
                    resp_data['errors'].append('No auth token returned.')
                    return json.dumps(resp_data), 500, headers

                else:
                    access_token = get_r['access_token']
                    auth = 'Bearer ' + access_token
                    from_address = req_data['templateParams']['from']

                    base_url = "https://graph.microsoft.com/v1.0/users/" + from_address + "/sendMail"
                    headers = {'Content-Type': 'application/json', 'Authorization': auth}

                    basedir = os.path.dirname(__file__)
                    real_path = "templates/automation.images/banner.png"
                    real_path_abs = os.path.join(basedir, real_path)

                    file = open(real_path_abs, 'rb')
                    file_read = file.read()
                    file_64_encode = base64.encodebytes(file_read)
                    file_encoded = file_64_encode.decode('ascii')

                    subject = req_data['templateParams']['subject']
                    subject = req_data['templateParams']['subject']

                    #   Uses jinja's 'safe' method in the template.  Be careful, we all any HTML here.
                    body = render_template("automation.html", body=req_data['body'])

        elif template_name == 'gis.service.disruption':
            pass
        elif template_name == 'gis.service.restoration':
            pass




PLEASE, TEST SEND EMAIL WITH AUTOMATION TEMPLATE

