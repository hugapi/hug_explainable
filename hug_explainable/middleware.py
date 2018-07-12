"""A hug middleware that automatically adds explanations to the request."""
import json

import hug

from hug_explainable.directive import Explainable

DOCUMENT = """
<html>
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Explanation</title>
        <style>
                    /* General Blueprint Style */
            @import url(http://fonts.googleapis.com/css?family=Lato:300,400,700);
            @font-face {
                font-family: 'bpicons';
                src:url('../fonts/bpicons/bpicons.eot');
                src:url('../fonts/bpicons/bpicons.eot?#iefix') format('embedded-opentype'),
                    url('../fonts/bpicons/bpicons.woff') format('woff'),
                    url('../fonts/bpicons/bpicons.ttf') format('truetype'),
                    url('../fonts/bpicons/bpicons.svg#bpicons') format('svg');
                font-weight: normal;
                font-style: normal;
            } /* Made with http://icomoon.io/ */

            *, *:after, *:before { -webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box; }
            body, html { font-size: 100%; padding: 0; margin: 0;}

            /* Clearfix hack by Nicolas Gallagher: http://nicolasgallagher.com/micro-clearfix-hack/ */
            .clearfix:before, .clearfix:after { content: " "; display: table; }
            .clearfix:after { clear: both; }

            body {
                font-family: 'Lato', Calibri, Arial, sans-serif;
                color: #47a3da;
            }

            a {
                color: #f0f0f0;
                text-decoration: none;
            }

            a:hover {
                color: #000;
            }

            .main,
            .container > header {
                width: 90%;
                max-width: 69em;
                margin: 0 auto;
                padding: 0 1.875em 3.125em 1.875em;
            }

            .container > header {
                padding: 2.875em 1.875em 1.875em;
            }

            .container > header h1 {
                font-size: 2.125em;
                line-height: 1.3;
                margin: 0 0 0.6em 0;
                float: left;
                font-weight: 400;
            }

            .container > header > span {
                display: block;
                position: relative;
                z-index: 9999;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.5em;
                padding: 0 0 0.6em 0.1em;
            }

            .container > header > span span:after {
                width: 30px;
                height: 30px;
                left: -12px;
                font-size: 50%;
                top: -8px;
                font-size: 75%;
                position: relative;
            }

            .container > header > span span:hover:before {
                content: attr(data-content);
                text-transform: none;
                text-indent: 0;
                letter-spacing: 0;
                font-weight: 300;
                font-size: 110%;
                padding: 0.8em 1em;
                line-height: 1.2;
                text-align: left;
                left: auto;
                margin-left: 4px;
                position: absolute;
                color: #fff;
                background: #47a3da;
            }

            .container > header nav {
                float: right;
                text-align: center;
            }

            .container > header nav a {
                display: inline-block;
                position: relative;
                text-align: left;
                width: 2.5em;
                height: 2.5em;
                background: #fff;
                border-radius: 50%;
                margin: 0 0.1em;
                border: 4px solid #47a3da;
            }

            .container > header nav a > span {
                display: none;
            }

            .container > header nav a:hover:before {
                content: attr(data-info);
                color: #47a3da;
                position: absolute;
                width: 600%;
                top: 120%;
                text-align: right;
                right: 0;
                pointer-events: none;
            }

            .container > header nav a:hover {
                background: #47a3da;
            }

            .bp-icon:after {
                font-family: 'bpicons';
                speak: none;
                font-style: normal;
                font-weight: normal;
                font-variant: normal;
                text-transform: none;
                text-align: center;
                color: #47a3da;
                -webkit-font-smoothing: antialiased;
            }

            .container > header nav .bp-icon:after {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                line-height: 2;
                text-indent: 0;
            }

            .container > header nav a:hover:after {
                color: #fff;
            }

            .bp-icon-next:after {
                content: "\e000";
            }
            .bp-icon-drop:after {
                content: "\e001";
            }
            .bp-icon-archive:after {
                content: "\e002";
            }
            .bp-icon-about:after {
                content: "\e003";
            }
            .bp-icon-prev:after {
                content: "\e004";
            }

            @media screen and (max-width: 55em) {

                .container > header h1,
                .container > header nav {
                    float: none;
                }

                .container > header > span,
                .container > header h1 {
                    text-align: center;
                }

                .container > header nav {
                    margin: 0 auto;
                }

                .container > header > span {
                    text-indent: 30px;
                }
            }

            @font-face {
                font-family: 'ecoico';
                src:url('../fonts/timelineicons/ecoico.eot');
                src:url('../fonts/timelineicons/ecoico.eot?#iefix') format('embedded-opentype'),
                    url('../fonts/timelineicons/ecoico.woff') format('woff'),
                    url('../fonts/timelineicons/ecoico.ttf') format('truetype'),
                    url('../fonts/timelineicons/ecoico.svg#ecoico') format('svg');
                font-weight: normal;
                font-style: normal;
            } /* Made with http://icomoon.io/ */

            .cbp_tmtimeline {
                margin: 30px 0 0 0;
                padding: 0;
                list-style: none;
                position: relative;
            }

            /* The line */
            .cbp_tmtimeline:before {
                content: '';
                position: absolute;
                top: 0;
                bottom: 0;
                width: 10px;
                background: #afdcf8;
                left: 20%;
                margin-left: -10px;
            }

            .cbp_tmtimeline > li {
                position: relative;
            }

            /* The date/time */
            .cbp_tmtimeline > li .cbp_tmtime {
                display: block;
                width: 25%;
                padding-right: 100px;
                position: absolute;
            }

            .cbp_tmtimeline > li .cbp_tmtime span {
                display: block;
                text-align: right;
            }

            .cbp_tmtimeline > li .cbp_tmtime span:first-child {
                font-size: 0.9em;
                color: #bdd0db;
            }

            .cbp_tmtimeline > li .cbp_tmtime span:last-child {
                font-size: 2.9em;
                color: #3594cb;
            }

            .cbp_tmtimeline > li:nth-child(odd) .cbp_tmtime span:last-child {
                color: #6cbfee;
            }

            /* Right content */
            .cbp_tmtimeline > li .cbp_tmlabel {
                margin: 0 0 15px 25%;
                background: #3594cb;
                color: #fff;
                padding: 2em;
                font-size: 1.2em;
                font-weight: 300;
                line-height: 1.4;
                position: relative;
                border-radius: 5px;
            }

            .cbp_tmtimeline > li:nth-child(odd) .cbp_tmlabel {
                background: #6cbfee;
            }

            .cbp_tmtimeline > li .cbp_tmlabel h2 {
                margin-top: 0px;
                padding: 0 0 10px 0;
                border-bottom: 1px solid rgba(255,255,255,0.4);
            }

            /* The triangle */
            .cbp_tmtimeline > li .cbp_tmlabel:after {
                right: 100%;
                border: solid transparent;
                content: " ";
                height: 0;
                width: 0;
                position: absolute;
                pointer-events: none;
                border-right-color: #3594cb;
                border-width: 10px;
                top: 10px;
            }

            .cbp_tmtimeline > li:nth-child(odd) .cbp_tmlabel:after {
                border-right-color: #6cbfee;
            }

            /* The icons */
            .cbp_tmtimeline > li .cbp_tmicon {
                width: 40px;
                height: 40px;
                font-family: 'ecoico';
                speak: none;
                font-style: normal;
                font-weight: normal;
                font-variant: normal;
                text-transform: none;
                font-size: 1.4em;
                line-height: 40px;
                -webkit-font-smoothing: antialiased;
                position: absolute;
                color: #fff;
                background: #46a4da;
                border-radius: 50%;
                box-shadow: 0 0 0 8px #afdcf8;
                text-align: center;
                left: 20%;
                top: 0;
                margin: 0 0 0 -25px;
            }

            .cbp_tmicon-phone:before {
                content: "\e000";
            }

            .cbp_tmicon-screen:before {
                content: "\e001";
            }

            .cbp_tmicon-mail:before {
                content: "\e002";
            }

            .cbp_tmicon-earth:before {
                content: "\e003";
            }

            /* Example Media Queries */
            @media screen and (max-width: 65.375em) {

                .cbp_tmtimeline > li .cbp_tmtime span:last-child {
                    font-size: 1.5em;
                }
            }

            @media screen and (max-width: 47.2em) {
                .cbp_tmtimeline:before {
                    display: none;
                }

                .cbp_tmtimeline > li .cbp_tmtime {
                    width: 100%;
                    position: relative;
                    padding: 0 0 20px 0;
                }

                .cbp_tmtimeline > li .cbp_tmtime span {
                    text-align: left;
                }

                .cbp_tmtimeline > li .cbp_tmlabel {
                    margin: 0 0 30px 0;
                    padding: 1em;
                    font-weight: 400;
                    font-size: 95%;
                }

                .cbp_tmtimeline > li .cbp_tmlabel:after {
                    right: auto;
                    left: 20px;
                    border-right-color: transparent;
                    border-bottom-color: #3594cb;
                    top: -20px;
                }

                .cbp_tmtimeline > li:nth-child(odd) .cbp_tmlabel:after {
                    border-right-color: transparent;
                    border-bottom-color: #6cbfee;
                }

                .cbp_tmtimeline > li .cbp_tmicon {
                    position: relative;
                    float: right;
                    left: auto;
                    margin: -55px 5px 0 0px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="main">
                <ul class="cbp_tmtimeline">
                    {content}
                </ul>
            </div>
        </div>
    </body>
</html>
"""
EXPLANATION = """
<li>
    <time class="cbp_tmtime" datetime="{datetime}"><span>{date}</span> <span>{time}</span></time>
    <div class="cbp_tmicon cbp_tmicon-screen"></div>
    <div class="cbp_tmlabel">
        <h2>{description}</h2>
        <pre>{data}</pre>
        <a href="{code_url}">
        {file}: {line}
        </a>
        <p>Took: {took}</p>
    </div>
</li>
"""


def init(api, option='explain', code_urls=None):
    @hug.request_middleware(api=api)
    def add_explain(request, response):
        should_explain = hug.types.smart_boolean(request.get_param('explain') or '.explain.' in request.path)
        response.context['explanation'] = Explainable(should_explain)

    @hug.response_middleware(api=api)
    def output_explain_if_requested(request, response, resource):
        if '.explain.' in request.path:
            if '.json' in request.path:
                response.content_type = 'application/json; charset=utf-8'
                response.body = hug.output_format.json(response.context['explanation'].explanation)
            elif '.html' in request.path:
                explanations = []
                response.content_type = 'text/html; charset=utf-8'
                for explanation in response.context['explanation'].explanation:
                    code_url = ''
                    for match, url in (code_urls or {}).items():
                        if match in explanation['file']:
                            code_url = url + explanation['file'].split(match)[-1]
                            break
                    explanations.append(EXPLANATION.format(data=json.dumps(explanation['value'], indent=4),
                                                            description=explanation['action'],
                                                            date=explanation['date'],
                                                            time=explanation['time'],
                                                            datetime=explanation['datetime'],
                                                            took=explanation['took'],
                                                            file=explanation['file'],
                                                            line=explanation['line'],
                                                            code_url=code_url))
                response.body = hug.output_format.html(DOCUMENT.replace('{content}', '\n'.join(explanations)))
