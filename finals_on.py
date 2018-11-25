from PIL import ImageEnhance
import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import Image
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from pubnub import Pubnub
import json
i=1
root = "C:\Python27\source" 
root2 ="C:\Python27\dest"

try:
   n = 0
   for dirpath, dirnames, filenames in os.walk(root):
    if n > 0 :
           for filename in filenames:
                LowerCaseFileName = filename.lower()
                abc=dirpath + "\\"
                fgt=abc+filename
                if LowerCaseFileName.endswith(".jpg"):
                    print 'xyz'
                    '''image = Image.open(fgt)
                    size = width, height= image.size
                    enhancer = ImageEnhance.Sharpness(image)
                    image = enhancer.enhance(20.0)
                    enhancer1 = ImageEnhance.Brightness(image)
                    image = enhancer1.enhance(2.0)
                    enhancer2 = ImageEnhance.Contrast(image)
                    image = enhancer2.enhance(10.0)
                    enhancer3 = ImageEnhance.Color(image)
                    image = enhancer3.enhance(2.0)
                    image.save("C:\Python27\dest\Dest2"+"\\"+filename)'''
                    print(filename)
                    '''image = Image.open(fgt)
                    size = width, height= image.size
                    cropped=image.crop((10,215,1180,528))
                    cropped.save(fgt)
                    img = cv2.imread(fgt,0)
                    cv2.imwrite(fgt,img)
                    im1=cv2.imread(fgt)
                    ret,thresh4 = cv2.threshold(im1,127,255,cv2.THRESH_TOZERO)
                    cv2.imwrite(fgt,thresh4)
                    im2=cv2.imread(fgt)
                    res=cv2.resize(im2,None,fx=1.5,fy=2,interpolation=cv2.INTER_LINEAR)'''
                    image = cv2.imread(fgt)
                    ratio = image.shape[0] / 500.0
                    orig = image.copy()
                    image = imutils.resize(image, height = 500)
                    x,y,w,h=0,0,0,0
                    largestarea=0
                    print ratio
 
                    # convert the image to grayscale, blur it, and find edges
                    # in the image
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    gray = cv2.GaussianBlur(gray, (5, 5), 0)
                    edged = cv2.Canny(gray, 0, 150, L2gradient=True)
 
                    # show the original image and the edge detected image
                    print "STEP 1: Edge Detection"
                    #cv2.imshow("Image", gray)
                    #cv2.imshow("Edged", edged)

                    # find the contours in the edged image, keeping only the
                    # largest ones, and initialize the screen contour
                    (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)

 
                    # loop over the contours
                    for c in cnts:
                        # approximate the contour
                        peri = cv2.arcLength(c, True)
                        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                        print len(approx)
                        #if len(approx)==4:
                        a=cv2.contourArea(approx)
                        print approx
   
                        print a
                        if(a>largestarea):
                            largestarea=a
                            screenCnt=approx
    
                            x,y,w,h=cv2.boundingRect(screenCnt)
                    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                    cropped=image[y:y+h,x:x+w]
    
 
                    # if our approximated contour has four points, then we
                    # can assume that we have found our screen
                    #if len(approx) == 4:
                    #print approx
                    #(x, y, w, h) = cv2.boundingRect(approx)
                        
                    #break
                    
                    # show the contour (outline) of the piece of paper
                    print "STEP 2: Find contours of paper"

                    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2) 
                    #cv2.imshow("Outline", image)


                    #warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

                    # convert the warped image to grayscale, then threshold it
                    # to give it that 'black and white' paper effect
                    #warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
                    #warped = cv2.adaptiveThreshold(warped,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
                    #warped = threshold_adaptive(warped, 251, offset = 10)
                    #warped = warped.astype("uint8") * 255

                    # show the original and scanned images
                    print "STEP 3: Apply perspective transform"
                    pts1 = np.float32([[x,y],[x+w,y],[x,y+h],[x+w,y+h]])
                    pts2 = np.float32([[0,0],[1000,0],[0,500],[1000,500]])
                    M = cv2.getPerspectiveTransform(pts1,pts2)
                    dst = cv2.warpPerspective(image,M,(1000,500))


                    cv2.imwrite(fgt,dst)
                    f=cv2.imread(fgt,0)
                    ret,thresh4 = cv2.threshold(f,127,255,cv2.THRESH_TOZERO)

                    cv2.imwrite(fgt,thresh4)
                    #cv2.imwrite("C:\Python27\done.jpg",cropped)
                    #cv2.imshow("Original", imutils.resize(orig, height = 650))
                    #cv2.imshow("Scanned", imutils.resize(warped, height = 650))
                    #cv2.waitKey(0)
                    #cv2.destroyAllWindows()


                    cv2.imwrite("/home/pi/Dest/Dest2"+"/"+filename,fgt)
                    '''enhancer = ImageEnhance.Sharpness(image)
                    image = enhancer.enhance(20.0)

                    enhancer1 = ImageEnhance.Brightness(image)
                    image = enhancer1.enhance(2.0)
                    enhancer2 = ImageEnhance.Contrast(image)
                    image = enhancer2.enhance(10.0)
                    enhancer3 = ImageEnhance.Color(image)
                    image = enhancer3.enhance(2.0)'''
                    #image.save("/home/pi/Dest/Dest2"+"/"+filename)
    n = n + 1
    print "images work done"
   n = 0
   for dirpath, dirnames, filenames in os.walk(root2):
    PdfOutputFileName = os.path.basename(dirpath) + ".pdf"
    c = canvas.Canvas(PdfOutputFileName)
    if n > 0 :
           for filename in filenames:
                LowerCaseFileName = filename.lower()
                if LowerCaseFileName.endswith(".jpg"):
                     filepath    = os.path.join(dirpath, filename)
                     im          = ImageReader(filepath)
                     imagesize   = im.getSize()
                     c.setPageSize(imagesize)
                     c.drawImage(filepath,0,0)
                     c.showPage()
                     c.save()
    n = n + 1
    print "PDF of Image directory created" + PdfOutputFileName
    i=0
except:
     print "Failed creating PDF"
if i==0:
   pubnub = Pubnub(publish_key="pub-c-e7aefd2c-f5e7-4a39-91bf-a7860668621e", subscribe_key="sub-c-30b188a6-405d-11e6-9c7c-0619f8945a4f")
   def _callback(message, channel):
        print(message)
        kk=json.dumps(message)
        kk=json.loads(kk)
        
        fromaddr = "abc@gmail.com"
        toaddr = kk['event']
    
        msg = MIMEMultipart()
    
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "SUBJECT OF THE EMAIL"
            
        body = "TEXT YOU WANT TO "
            
        msg.attach(MIMEText(body, 'plain'))
            
        filename = "project report.pdf"
        attachment = open(PdfOutputFileName, "rb")
            
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            
        msg.attach(part)
            
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromaddr, "PASSWORD")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
   def _error(message):
        print(message)

   pubnub.subscribe(channels="tu", callback=_callback, error=_error)
