# Creating a custom HTTP header response with Puppet
exec {'HTTP_header':
    provider => shell,
    command => 'sudo sed -i "s/http {/http {\n\n\tadd_header X-Served-By $hostname;\n/" /etc/nginx/nginx.conf ; sudo service nginx reload',
}
