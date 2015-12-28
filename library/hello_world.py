#!/usr/bin/python

import json
import os

def main():
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True),
            port=dict(required=True, type='int'),
            timeout=dict(required=False, type='int', default=1)
        ),
        supports_check_mode=True)

    module.exit_json(failed=True)
    #module.fail_json()
    if module.check_mode:
        module.exit_json(changed=False)
    module.exit_json(changed=True)

with open(__file__, 'r') as f, \
        open('/tmp/a', 'w') as f2:
    f2.write(f.read())

from ansible.module_utils.basic import *
main()
