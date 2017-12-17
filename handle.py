# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import reply
import receive
import web
from getData import *
class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                	if recMsg.Content == '温度':
				content = str(getData_time('temperature'))+'\n室内温度为'+str(getData_value('temperature')) +'℃'
		  	elif recMsg.Content == '湿度':
				content = str(getData_time('humidity'))+'\n室内湿度为'+str(getData_value('humidity')) +'%'
			else:
				content = '抱歉尚未开通这项指令功能，你可以尝试发送‘温度’、‘湿度’来查看最新的室内信息,或者发送相应的语音消息 '
                   	replyMsg = reply.TextMsg(toUser, fromUser, content)
                   	return replyMsg.send()
                if recMsg.MsgType == 'voice':
                    	if recMsg.Recognition =='温度。':
				content = str(getData_time('temperature'))+'\n室内温度为'+str(getData_value('temperature')) +'℃'
			elif recMsg.Recognition =='湿度。':
				content = str(getData_time('humidity'))+'\n室内湿度为'+str(getData_value('humidity')) +'%'
			else:
				content =recMsg.Recognition+'\n无法识别这条语音消息'
                    	replyMsg = reply.TextMsg(toUser, fromUser, content)
                    	return replyMsg.send()
                else:
                    	return reply.Msg().send()
            else:
                print "暂且不处理"
                return reply.Msg().send()
        except Exception, Argment:
            return Argment
