import os,platform
if platform.system() == "Linux":
	print "Linux"
elif platform.system() == "Darwin":
	print "Darwin"
elif platform.system() == "SunOS":
	print "SunOS"
elif platform.system() == "FreeBSD":
	print "FreeBSD"
elif platform.system() == "Unix":
	print "Unix"
elif platform.system() == "OpenBSD":
	print "OpenBSD"
elif platform.system() == "NetBSD":
	print "NetBSD"
elif platform.system() == "Windows":
	print "Windows"
else:
	print "else"
