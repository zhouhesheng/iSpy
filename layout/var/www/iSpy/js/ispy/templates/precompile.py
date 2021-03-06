#!/usr/bin/env python
'''
This will eventually get replaced with Require.js
but until then it's a quick hack to save time.
'''

import os

EXIT_SUCCESS = 0


def precompile(compiler='handlebars'):
    '''
    Quick hack to precompile all templates
    '''
    success = 0
    print("[*] Precompiling templates, please wait ...")
    files = filter(
        lambda f: f.endswith('.handlebars'), os.listdir('./handlebars'))
    for hb in files:
        output = ''.join(hb.split('.')[:-1]) + '.js'
        exit_status = os.system('%s ./handlebars/%s -f ./js/%s' % (
            compiler, hb, output
        ))
        if exit_status == EXIT_SUCCESS:
            print("[$] Successfully compiled %s" % hb)
            success += 1
        else:
            print("[!] Failed to compile %s" % hb)
    print("[*] Successfully compiled %d of %d templates" % (
        success, len(files)
    ))
    if success == len(files):
        minify()


def minify(minifier='minify', output='templates.min.js'):
    print("[*] Minifying JavaScript files ...")
    files = filter(lambda f: f.endswith('.js'), os.listdir('./js'))
    if output in files:
        files.remove(output)
    os.system("%s ./js/%s > %s" % (
        minifier, " ./js/".join(files), './js/' + output,
    ))
    os.system("rm ./js/%s" % " ./js/".join(files))


if __name__ == '__main__':
    precompile()
