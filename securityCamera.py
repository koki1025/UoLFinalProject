from picamera.array import PiRGBArray
import cv2
from picamera2 import Picamera2
from libcamera import controls

import requests

import time
import urllib
import urllib.request
import urllib.error
import json
import ssl
import RPi.GPIO as GPIO




cv2.startWindowThread()

picam2 = Picamera2()
rawCapture = PiRGBArray(picam2, size=(640,480))
time.sleep(0.1)

picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})

face_date = []

faceCascade = cv2.CascadeClassifier("/usr/local/lib/python3.9/dist-packages/cv2/data/""haarcascade_frontalface_alt.xml")

print("done here")
# 顔を認識した場合にAzure Machine Learningにデータを送信する処理
# for frame in picam2.capture_array(rawCapture, format="bgr", use_video_port=True):
while True:
    image = picam2.capture_array()
 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    

    # 顔を四角枠で囲う
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


   # フレームを表示
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF


    # 次のフレームを表示
    rawCapture.truncate(0)


    # ［Q］キーでストップ
    if key == ord("q"):
        break


    # 顔を認識し矩形にリスト化
    face_list = faceCascade.detectMultiScale(image)
#     print("face_list", face_list)

    if len(face_list) > 0:
        for face in face_list:
            image = image[face[1]:face[1] + face[3], face[0]:face[0] + face[2]] # トリミング 例：[68:218 , 55:205]
            image = cv2.resize(image, (28, 28)) # リサイズ
            image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # グレースケール
            image_gs = image_gs.flatten() # リストを平坦化
            i= 1
            for n in image_gs:
                exec("img%d = %d" % (i, n))
                i = i+1
        ssl._create_default_https_context = ssl._create_unverified_context
        data = {
            "Inputs": {
                "input1":
                    {
                        "ColumnNames": ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8", "Col9", "Col10", "Col11", "Col12", "Col13", "Col14", "Col15", "Col16", "Col17", "Col18", "Col19", "Col20", "Col21", "Col22", "Col23", "Col24", "Col25", "Col26", "Col27", "Col28", "Col29", "Col30", "Col31", "Col32", "Col33", "Col34", "Col35", "Col36", "Col37", "Col38", "Col39", "Col40", "Col41", "Col42", "Col43", "Col44", "Col45", "Col46", "Col47", "Col48", "Col49", "Col50", "Col51", "Col52", "Col53", "Col54", "Col55", "Col56", "Col57", "Col58", "Col59", "Col60", "Col61", "Col62", "Col63", "Col64", "Col65", "Col66", "Col67", "Col68", "Col69", "Col70", "Col71", "Col72", "Col73", "Col74", "Col75", "Col76", "Col77", "Col78", "Col79", "Col80", "Col81", "Col82", "Col83", "Col84", "Col85", "Col86", "Col87", "Col88", "Col89", "Col90", "Col91", "Col92", "Col93", "Col94", "Col95", "Col96", "Col97", "Col98", "Col99", "Col100", "Col101", "Col102", "Col103", "Col104", "Col105", "Col106", "Col107", "Col108", "Col109", "Col110", "Col111", "Col112", "Col113", "Col114", "Col115", "Col116", "Col117", "Col118", "Col119", "Col120", "Col121", "Col122", "Col123", "Col124", "Col125", "Col126", "Col127", "Col128", "Col129", "Col130", "Col131", "Col132", "Col133", "Col134", "Col135", "Col136", "Col137", "Col138", "Col139", "Col140", "Col141", "Col142", "Col143", "Col144", "Col145", "Col146", "Col147", "Col148", "Col149", "Col150", "Col151", "Col152", "Col153", "Col154", "Col155", "Col156", "Col157", "Col158", "Col159", "Col160", "Col161", "Col162", "Col163", "Col164", "Col165", "Col166", "Col167", "Col168", "Col169", "Col170", "Col171", "Col172", "Col173", "Col174", "Col175", "Col176", "Col177", "Col178", "Col179", "Col180", "Col181", "Col182", "Col183", "Col184", "Col185", "Col186", "Col187", "Col188", "Col189", "Col190", "Col191", "Col192", "Col193", "Col194", "Col195", "Col196", "Col197", "Col198", "Col199", "Col200", "Col201", "Col202", "Col203", "Col204", "Col205", "Col206", "Col207", "Col208", "Col209", "Col210", "Col211", "Col212", "Col213", "Col214", "Col215", "Col216", "Col217", "Col218", "Col219", "Col220", "Col221", "Col222", "Col223", "Col224", "Col225", "Col226", "Col227", "Col228", "Col229", "Col230", "Col231", "Col232", "Col233", "Col234", "Col235", "Col236", "Col237", "Col238", "Col239", "Col240", "Col241", "Col242", "Col243", "Col244", "Col245", "Col246", "Col247", "Col248", "Col249", "Col250", "Col251", "Col252", "Col253", "Col254", "Col255", "Col256", "Col257", "Col258", "Col259", "Col260", "Col261", "Col262", "Col263", "Col264", "Col265", "Col266", "Col267", "Col268", "Col269", "Col270", "Col271", "Col272", "Col273", "Col274", "Col275", "Col276", "Col277", "Col278", "Col279", "Col280", "Col281", "Col282", "Col283", "Col284", "Col285", "Col286", "Col287", "Col288", "Col289", "Col290", "Col291", "Col292", "Col293", "Col294", "Col295", "Col296", "Col297", "Col298", "Col299", "Col300", "Col301", "Col302", "Col303", "Col304", "Col305", "Col306", "Col307", "Col308", "Col309", "Col310", "Col311", "Col312", "Col313", "Col314", "Col315", "Col316", "Col317", "Col318", "Col319", "Col320", "Col321", "Col322", "Col323", "Col324", "Col325", "Col326", "Col327", "Col328", "Col329", "Col330", "Col331", "Col332", "Col333", "Col334", "Col335", "Col336", "Col337", "Col338", "Col339", "Col340", "Col341", "Col342", "Col343", "Col344", "Col345", "Col346", "Col347", "Col348", "Col349", "Col350", "Col351", "Col352", "Col353", "Col354", "Col355", "Col356", "Col357", "Col358", "Col359", "Col360", "Col361", "Col362", "Col363", "Col364", "Col365", "Col366", "Col367", "Col368", "Col369", "Col370", "Col371", "Col372", "Col373", "Col374", "Col375", "Col376", "Col377", "Col378", "Col379", "Col380", "Col381", "Col382", "Col383", "Col384", "Col385", "Col386", "Col387", "Col388", "Col389", "Col390", "Col391", "Col392", "Col393", "Col394", "Col395", "Col396", "Col397", "Col398", "Col399", "Col400", "Col401", "Col402", "Col403", "Col404", "Col405", "Col406", "Col407", "Col408", "Col409", "Col410", "Col411", "Col412", "Col413", "Col414", "Col415", "Col416", "Col417", "Col418", "Col419", "Col420", "Col421", "Col422", "Col423", "Col424", "Col425", "Col426", "Col427", "Col428", "Col429", "Col430", "Col431", "Col432", "Col433", "Col434", "Col435", "Col436", "Col437", "Col438", "Col439", "Col440", "Col441", "Col442", "Col443", "Col444", "Col445", "Col446", "Col447", "Col448", "Col449", "Col450", "Col451", "Col452", "Col453", "Col454", "Col455", "Col456", "Col457", "Col458", "Col459", "Col460", "Col461", "Col462", "Col463", "Col464", "Col465", "Col466", "Col467", "Col468", "Col469", "Col470", "Col471", "Col472", "Col473", "Col474", "Col475", "Col476", "Col477", "Col478", "Col479", "Col480", "Col481", "Col482", "Col483", "Col484", "Col485", "Col486", "Col487", "Col488", "Col489", "Col490", "Col491", "Col492", "Col493", "Col494", "Col495", "Col496", "Col497", "Col498", "Col499", "Col500", "Col501", "Col502", "Col503", "Col504", "Col505", "Col506", "Col507", "Col508", "Col509", "Col510", "Col511", "Col512", "Col513", "Col514", "Col515", "Col516", "Col517", "Col518", "Col519", "Col520", "Col521", "Col522", "Col523", "Col524", "Col525", "Col526", "Col527", "Col528", "Col529", "Col530", "Col531", "Col532", "Col533", "Col534", "Col535", "Col536", "Col537", "Col538", "Col539", "Col540", "Col541", "Col542", "Col543", "Col544", "Col545", "Col546", "Col547", "Col548", "Col549", "Col550", "Col551", "Col552", "Col553", "Col554", "Col555", "Col556", "Col557", "Col558", "Col559", "Col560", "Col561", "Col562", "Col563", "Col564", "Col565", "Col566", "Col567", "Col568", "Col569", "Col570", "Col571", "Col572", "Col573", "Col574", "Col575", "Col576", "Col577", "Col578", "Col579", "Col580", "Col581", "Col582", "Col583", "Col584", "Col585", "Col586", "Col587", "Col588", "Col589", "Col590", "Col591", "Col592", "Col593", "Col594", "Col595", "Col596", "Col597", "Col598", "Col599", "Col600", "Col601", "Col602", "Col603", "Col604", "Col605", "Col606", "Col607", "Col608", "Col609", "Col610", "Col611", "Col612", "Col613", "Col614", "Col615", "Col616", "Col617", "Col618", "Col619", "Col620", "Col621", "Col622", "Col623", "Col624", "Col625", "Col626", "Col627", "Col628", "Col629", "Col630", "Col631", "Col632", "Col633", "Col634", "Col635", "Col636", "Col637", "Col638", "Col639", "Col640", "Col641", "Col642", "Col643", "Col644", "Col645", "Col646", "Col647", "Col648", "Col649", "Col650", "Col651", "Col652", "Col653", "Col654", "Col655", "Col656", "Col657", "Col658", "Col659", "Col660", "Col661", "Col662", "Col663", "Col664", "Col665", "Col666", "Col667", "Col668", "Col669", "Col670", "Col671", "Col672", "Col673", "Col674", "Col675", "Col676", "Col677", "Col678", "Col679", "Col680", "Col681", "Col682", "Col683", "Col684", "Col685", "Col686", "Col687", "Col688", "Col689", "Col690", "Col691", "Col692", "Col693", "Col694", "Col695", "Col696", "Col697", "Col698", "Col699", "Col700", "Col701", "Col702", "Col703", "Col704", "Col705", "Col706", "Col707", "Col708", "Col709", "Col710", "Col711", "Col712", "Col713", "Col714", "Col715", "Col716", "Col717", "Col718", "Col719", "Col720", "Col721", "Col722", "Col723", "Col724", "Col725", "Col726", "Col727", "Col728", "Col729", "Col730", "Col731", "Col732", "Col733", "Col734", "Col735", "Col736", "Col737", "Col738", "Col739", "Col740", "Col741", "Col742", "Col743", "Col744", "Col745", "Col746", "Col747", "Col748", "Col749", "Col750", "Col751", "Col752", "Col753", "Col754", "Col755", "Col756", "Col757", "Col758", "Col759", "Col760", "Col761", "Col762", "Col763", "Col764", "Col765", "Col766", "Col767", "Col768", "Col769", "Col770", "Col771", "Col772", "Col773", "Col774", "Col775", "Col776", "Col777", "Col778", "Col779", "Col780", "Col781", "Col782", "Col783", "Col784", "Col785"],
                        "Values": [ [ "0", img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16, img17, img18, img19, img20, img21, img22, img23, img24, img25, img26, img27, img28, img29, img30, img31, img32, img33, img34, img35, img36, img37, img38, img39, img40, img41, img42, img43, img44, img45, img46, img47, img48, img49, img50, img51, img52, img53, img54, img55, img56, img57, img58, img59, img60, img61, img62, img63, img64, img65, img66, img67, img68, img69, img70, img71, img72, img73, img74, img75, img76, img77, img78, img79, img80, img81, img82, img83, img84, img85, img86, img87, img88, img89, img90, img91, img92, img93, img94, img95, img96, img97, img98, img99, img100, img101, img102, img103, img104, img105, img106, img107, img108, img109, img110, img111, img112, img113, img114, img115, img116, img117, img118, img119, img120, img121, img122, img123, img124, img125, img126, img127, img128, img129, img130, img131, img132, img133, img134, img135, img136, img137, img138, img139, img140, img141, img142, img143, img144, img145, img146, img147, img148, img149, img150, img151, img152, img153, img154, img155, img156, img157, img158, img159, img160, img161, img162, img163, img164, img165, img166, img167, img168, img169, img170, img171, img172, img173, img174, img175, img176, img177, img178, img179, img180, img181, img182, img183, img184, img185, img186, img187, img188, img189, img190, img191, img192, img193, img194, img195, img196, img197, img198, img199, img200, img201, img202, img203, img204, img205, img206, img207, img208, img209, img210, img211, img212, img213, img214, img215, img216, img217, img218, img219, img220, img221, img222, img223, img224, img225, img226, img227, img228, img229, img230, img231, img232, img233, img234, img235, img236, img237, img238, img239, img240, img241, img242, img243, img244, img245, img246, img247, img248, img249, img250, img251, img252, img253, img254, img255, img256, img257, img258, img259, img260, img261, img262, img263, img264, img265, img266, img267, img268, img269, img270, img271, img272, img273, img274, img275, img276, img277, img278, img279, img280, img281, img282, img283, img284, img285, img286, img287, img288, img289, img290, img291, img292, img293, img294, img295, img296, img297, img298, img299, img300, img301, img302, img303, img304, img305, img306, img307, img308, img309, img310, img311, img312, img313, img314, img315, img316, img317, img318, img319, img320, img321, img322, img323, img324, img325, img326, img327, img328, img329, img330, img331, img332, img333, img334, img335, img336, img337, img338, img339, img340, img341, img342, img343, img344, img345, img346, img347, img348, img349, img350, img351, img352, img353, img354, img355, img356, img357, img358, img359, img360, img361, img362, img363, img364, img365, img366, img367, img368, img369, img370, img371, img372, img373, img374, img375, img376, img377, img378, img379, img380, img381, img382, img383, img384, img385, img386, img387, img388, img389, img390, img391, img392, img393, img394, img395, img396, img397, img398, img399, img400, img401, img402, img403, img404, img405, img406, img407, img408, img409, img410, img411, img412, img413, img414, img415, img416, img417, img418, img419, img420, img421, img422, img423, img424, img425, img426, img427, img428, img429, img430, img431, img432, img433, img434, img435, img436, img437, img438, img439, img440, img441, img442, img443, img444, img445, img446, img447, img448, img449, img450, img451, img452, img453, img454, img455, img456, img457, img458, img459, img460, img461, img462, img463, img464, img465, img466, img467, img468, img469, img470, img471, img472, img473, img474, img475, img476, img477, img478, img479, img480, img481, img482, img483, img484, img485, img486, img487, img488, img489, img490, img491, img492, img493, img494, img495, img496, img497, img498, img499, img500, img501, img502, img503, img504, img505, img506, img507, img508, img509, img510, img511, img512, img513, img514, img515, img516, img517, img518, img519, img520, img521, img522, img523, img524, img525, img526, img527, img528, img529, img530, img531, img532, img533, img534, img535, img536, img537, img538, img539, img540, img541, img542, img543, img544, img545, img546, img547, img548, img549, img550, img551, img552, img553, img554, img555, img556, img557, img558, img559, img560, img561, img562, img563, img564, img565, img566, img567, img568, img569, img570, img571, img572, img573, img574, img575, img576, img577, img578, img579, img580, img581, img582, img583, img584, img585, img586, img587, img588, img589, img590, img591, img592, img593, img594, img595, img596, img597, img598, img599, img600, img601, img602, img603, img604, img605, img606, img607, img608, img609, img610, img611, img612, img613, img614, img615, img616, img617, img618, img619, img620, img621, img622, img623, img624, img625, img626, img627, img628, img629, img630, img631, img632, img633, img634, img635, img636, img637, img638, img639, img640, img641, img642, img643, img644, img645, img646, img647, img648, img649, img650, img651, img652, img653, img654, img655, img656, img657, img658, img659, img660, img661, img662, img663, img664, img665, img666, img667, img668, img669, img670, img671, img672, img673, img674, img675, img676, img677, img678, img679, img680, img681, img682, img683, img684, img685, img686, img687, img688, img689, img690, img691, img692, img693, img694, img695, img696, img697, img698, img699, img700, img701, img702, img703, img704, img705, img706, img707, img708, img709, img710, img711, img712, img713, img714, img715, img716, img717, img718, img719, img720, img721, img722, img723, img724, img725, img726, img727, img728, img729, img730, img731, img732, img733, img734, img735, img736, img737, img738, img739, img740, img741, img742, img743, img744, img745, img746, img747, img748, img749, img750, img751, img752, img753, img754, img755, img756, img757, img758, img759, img760, img761, img762, img763, img764, img765, img766, img767, img768, img769, img770, img771, img772, img773, img774, img775, img776, img777, img778, img779, img780, img781, img782, img783, img784 ], ]
                    }, },
            "GlobalParameters": {
            }
        }
        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/f3e7141893264483840909a0cf52541c/services/b021a663b59542ab89ab7ba5229df230/execute?api-version=2.0&details=true'
        api_key = 'liMHbEl8mrBgYhuwZ1cMhDtIu8yNMD2KDMO7o9vaO5dKKHXQlr4fNzrRn5wSPGCR4CyABumoPW4i+AMCLQJMiA=='
        headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
        req = urllib.request.Request(url, body, headers)
        try:
            response = urllib.request.urlopen(req)
            result = response.read().decode("utf-8")
            json_str = result
            json_dict = json.loads(json_str)
            output1 = json_dict["Results"]["output1"]["value"]["Values"]
            last_val = output1[0][-1]
            
            print('response', response)
            print('result', result)
            print('json_str', json_str)
            print('output1',output1)

            print(last_val)
            print("人を認識しました。")
            if last_val == "0":
                print("不審者")

                GPIO.setmode(GPIO.BCM) # ピン番号ではなくGPIOの番号で指定
                GPIO.setup(21, GPIO.OUT) # GPIO 21を出力として指定
                
                # 繰り返し処理
                for l in range(2):
                    GPIO.output(21, GPIO.HIGH) # GPIO 21をHIGHに変更
                    time.sleep(0.5) # 0.5秒停止
                    GPIO.output(21, GPIO.LOW) # GPIO 21をLOWに変更
                    time. sleep(0.5) # 0.5秒停止
                # IFTTT
                requests.post("https://maker.ifttt.com/trigger/suspicious_person/json/with/key/d1utZFpUCY0_OcU7jfEuB85ckz02mv4TKEpC_EjO7QO")
            else:
                print("一般人")
            time.sleep(1)

        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))
            print(error.info())
            print(json.loads(error.read()))

    face_list = []

print("End while")
picam2.stop()
cv2.destroyAllWindows()

