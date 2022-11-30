# Automate the fixing of Apache 500 error.

exec { 'replace_phpp_with_php':
    provider => shell,
    command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"; 'service apache2 reload',
}
