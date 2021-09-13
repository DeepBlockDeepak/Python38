import traceback #needed when using "except:" on line 6

try:
    raise Exception("This is the error message. Hallelujah Satan")

except Exception as err:    # alternatively, just use--->  except:
                            #if using ---> except: ---> follow with ---> errorFile.write(traceback.format_exc())
    errorFile = open("errorinfo.txt", 'w')
    errorFile.write(str(err))   #must use str() on 'err' 
    #errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written to errorInfo.txt")
