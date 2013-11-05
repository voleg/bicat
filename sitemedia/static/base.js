/**
 * Created by voleg on 01.11.13.
 */
$('.nav li').each(function () {
                    var link = $('a', $(this)).attr('href');
                    if (typeof link == 'undefined') return;
                    var path = window.location.pathname;
                    if (link == path || path.indexOf(link) == 0 || path.indexOf(link.replace('s/', '/')) == 0) {
                        $('#id_menu_div').find('li').removeClass('active');
                        $(this).addClass('active');
                    }
                });

$("[data-toggle=tooltip]").tooltip();
