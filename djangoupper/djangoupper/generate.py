import sys
if len(sys.argv)<=1:
	print("provide path to model.py")
	sys.exit()

choice = False
create=False
read=False
update=False
delete=False
if len(sys.argv) == 3:
	choice = True
	choicstring = sys.argv[2]
	if "C" in choicstring:
		create=True
	if "R" in choicstring:
		read=True
	if "U" in choicstring:
		update=True
	if "D" in choicstring:
		delete=True

completename = sys.argv[1]
directoryname = ""
if "/" in completename:
	id = completename.find("/")
	directoryname = completename[0:id].strip()
	directoryname += "/"

file = open(sys.argv[1], "r")
modelines = file.readlines()
modelfields = {}
listfields = []
models = []
for i in modelines:
	fields = []
	modelname = ""
	if "models.Model" in i:
		endpoint = i.find("(")
		# print(endpoint)
		modelname = i[5:endpoint].strip()
		models.append(modelname)

	if "= models." in i:
		endpoint = i.find("=")
		if endpoint!=-1:
			field = i[0:endpoint].strip()
			fields.append(field)
	if modelname:
		modelfields[modelname]=fields
	

serializers = []
serializers.append("# generated serializers")
serializers.append("from " + directoryname + ".models import *")
serializers.append("from rest_framework import serializers")

for i in models:
	serializers.append("class " + i + "DetailSerializer(serializers.ModelSerializer):")
	serializers.append("  # detail serializer")
	serializers.append("  class Meta:")
	serializers.append("    model = " + i)
	fieldstring = "    fields = ["
	for j in range(0, len(modelfields[i])):
		if j != len(modelfields[i]) - 1:
			fieldstring = fieldstring + modelfields[i][j] + ","
		else:
			fieldstring = fieldstring + modelfields[i][j]
	fieldstring += "]"
	serializers.append(fieldstring)

	serializers.append("");
	serializers.append("class " + i + "CreateUpdateSerializer(serializers.ModelSerializer):")
	serializers.append("  # create update serializer")
	serializers.append("  class Meta:")
	serializers.append("    model = " + i)
	serializers.append(fieldstring)
	serializers.append("");

file=open(directoryname+'serializers.py', "a+")
for i in serializers:
	file.write(i+"\n")
file.close()

print("# generated serializers and generic api views")
apiviews = []
apiviews.append("from rest_framework.generics import *")
apiviews.append("from " + directoryname + ".models import *")
apiviews.append("from .serializers import *")

for i in models:
	if not choice or ( choice and read ):
		apiviews.append("class " + i +"ListAPIView(ListAPIView):")
		apiviews.append("  # list api view")
		apiviews.append("  queryset = " + i +".objects.all()")
		apiviews.append("  serializer_class = "+ i + "DetailSerializer")
		apiviews.append("")

		apiviews.append("class " + i +"DetailAPIView(RetrieveAPIView):")
		apiviews.append("  # detail api view")
		apiviews.append("  queryset = " + i +".objects.all()")
		apiviews.append("  serializer_class = "+ i + "DetailSerializer")
		apiviews.append("")

	if not choice or ( choice and read ):
		apiviews.append("class " + i +"CreateAPIView(CreateAPIView):")
		apiviews.append("  # create api view")
		apiviews.append("  queryset = " + i +".objects.all()")
		apiviews.append("  serializer_class = "+ i + "CreateUpdateSerializer")
		apiviews.append("")

	if not choice or ( choice and update ):
		apiviews.append("class " + i +"UpdateAPIView(UpdateAPIView):")
		apiviews.append("  # update api view")
		apiviews.append("  queryset = " + i +".objects.all()")
		apiviews.append("  serializer_class = "+ i + "CreateUpdateSerializer")
		apiviews.append("")

	if not choice or ( choice and delete ):
		apiviews.append("class " + i +"DeleteAPIView(DestroyAPIView):")
		apiviews.append("  # delete api view")
		apiviews.append("  queryset = " + i +".objects.all()")
		apiviews.append("  serializer_class = "+ i + "DetailSerializer")
		apiviews.append("")

file=open(directoryname+'views.py', 'a+')
for i in apiviews:
	file.write(i+"\n")
file.close()