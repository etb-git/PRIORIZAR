
import pandas as pd
import re

### prueba





 
def clean_text(text):
  

    text=re.sub(r'No exitoso - RF-', "otros", text) 
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', re.sub(r'[áéíóú]', lambda m: {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}[m.group(0)], text))
  
    text =re.sub(r'ù', 'u', text)
    text = re.sub(r"[0-9]", "", text)

    #text = re.sub(r"Motivo de llamada:\s*(.*)", r'\1', text)


    #text=re.sub(r'^.*?(MOTIVO:)', r'\1', text)

    
    

    text=re.sub(r'^.*?cuenta de facturacion\s*',"",text, flags=re.IGNORECASE)
    text=re.sub(r'^.*?solicitud del cliente\s*',"",text, flags=re.IGNORECASE)
    text=re.sub(r'^.*?cuenta:\s*',"",text, flags=re.IGNORECASE)

    text=re.sub(r'^.*?cedula de ciudadania\s*',"",text, flags=re.IGNORECASE)
    text=re.sub(r'^.*?//cliente\s*',"",text, flags=re.IGNORECASE)

    text=re.sub(r'^.*?aseg//*',"",text, flags=re.IGNORECASE)
   
    text=re.sub(r'^.*?motivo de retiro\s*',"",text, flags=re.IGNORECASE)
    text=re.sub(r'^.*?motivo de llamada\s*',"",text, flags=re.IGNORECASE)
    text=re.sub(r'^.*?motivo de la llamada\s*',"",text, flags=re.IGNORECASE)
    text=re.sub(r'^.*?motivo\s*',"",text, flags=re.IGNORECASE)



    text =re.sub(r'\b\w*gmail\w*\b', '', text)
    text =re.sub(r'\b\w*hotmail\w*\b', '', text)


   
    text=re.sub(r'noviembre', "", text)
    text=re.sub(r'diciembre', "", text)
    text=re.sub(r'febrero', "", text)
    #text=re.sub(r'enero', "", text)
    text=re.sub(r'marzo', "", text)
    text=re.sub(r'abril', "", text)
    text=re.sub(r'mayo', "", text)
    text=re.sub(r'junio', "", text)
    text=re.sub(r'julio', "", text)
    text=re.sub(r'agosto', "", text)
    text=re.sub(r'mayo', "", text)
    text=re.sub(r'septiembre', "", text)
    text=re.sub(r'noviembre', "", text)
    text=re.sub(r'diciembre', "", text)
    text=re.sub(r'octubre', "", text)
    text=re.sub(r'iva', "", text)
    
    
    text=re.sub(r'pretensión', "pretension", text)


    
    text=re.sub(r'^.*?(ASUNTO:)', r'\1', text)
    text=re.sub(r'^.*?(descripcion:)', r'\1', text)
    text=re.sub(r'^.*?(\\ cliente)', r'\1', text)


    text=re.sub(r'^.*?(FACTURADOS,)', r'\1', text)
    text=re.sub(r'^.*?(APP MIETB//)', r'\1', text)

    

    text=re.sub(r'\baseg lt\b', '', text)
    


 
    text = re.sub(r"linea", "", text)
    
    text = re.sub(r"LEY 1755", "", text)
    text = re.sub(r"Ley 1755", "", text)
    text = re.sub(r"ID", "", text)
    
    text = re.sub(r"numeor", "", text)
    text = re.sub(r"MDM-FIBRA-", "", text)
    text=re.sub(r'^.*?de la llamada\s*', "", text)
    text = re.sub(r'linea', '', text)
    text = re.sub(r'back', '', text)
    text = re.sub(r'Cuenta', '', text)
    text = re.sub(r'CELULAR', '', text)
    text = re.sub(r'Nombre', '', text)
    text = re.sub(r'CLIENTE', '', text)
    text = re.sub(r'RF-', '', text)
    text = re.sub(r'Notas de Escalamiento', '', text)
    text = re.sub(r'Milena', '', text)
    text = re.sub(r'x000D', '', text)
    text = re.sub(r'Asg_Comdata_Caso_', '', text)
    text = re.sub(r'CLT ', '', text)
    text = re.sub(r'GESTION PROACTIVA', '', text)
    text = re.sub(r'lte', '', text)
    text = re.sub(r'whatsapp', '', text)
    text = re.sub(r'DOCUMENTO', '', text)
    text = re.sub(r'Número contacto', '', text)
    text = re.sub(r'NA', '', text)
    text = re.sub(r'Motivo de la llamada:', '', text)
    text = re.sub(r'N/A', '', text)
    text = re.sub(r'facebook', '', text)
    text = re.sub(r'TWNogard_ilustra', '', text)
    text = re.sub(r'RRSS', '', text)
    text = re.sub(r'TITULAR', '', text)
    text = re.sub(r'MOTIVO RETIRO', '', text)
    text = re.sub(r'MIXTO', '', text)
    text = re.sub(r'razón', 'razon', text)

    text = re.sub(r"reinicia", "reiniciar", text)
    text = re.sub(r"reset", "reiniciar", text)
    text = re.sub(r"arear", "area", text)
    text = re.sub(r"trasfierir", "transferir", text)
    
 
    text = re.sub(r"tegnicas", "tecnicas", text)
    
    text = re.sub(r"visita tecnica", " visita", text)
    text = re.sub(r"reiniciarr", "reiniciar", text)
    text = re.sub(r"celular", "", text)
    text = re.sub(r"servicios", "servicio", text)
    text = re.sub(r"wifi", "wiffi", text)
    text = re.sub(r"kr", " ", text)
    text = re.sub(r"validan", "valida", text)
   
    #text = re.sub(r"go", "directvgo", text)
    text = re.sub(r"agendamiento", "agenda", text)
    text = re.sub(r"moden", "modem", text)
    text = re.sub(r"/", " ", text)

    text = re.sub(r"información", "informacion", text)
    text = re.sub(r"explicacion", "informacion", text)
    text = re.sub(r"explicación", "informacion", text)
    text = re.sub(r"explicar", "informacion", text)
    
    

     

    
    

    
    
    text = re.sub(r"Gracias por preferirnos y darnos la confianza de ser su proveedor de comunicaciones, estamos seguros de que ha escogido la mejor opción. En ETB trabajamos día a día para que nuestros productos y servicios sean de la mejor calidad, para usted y su Familia", "", text)
    
    #text = re.sub(r"reinicia", "reiniciar", text)
  
    

    #text = re.sub(r"$", "", text)

    
    text = re.sub(r"primer nivel", "primernivel", text)
    text = re.sub(r"soporte primer nivel", "primernivel", text)
    text = re.sub(r" ________________________________________", "", text)
    text = re.sub(r"__________________________", "", text)
    text=re.sub("(\s\d+)"," ",text)
    text = re.sub(r"cc", " ", text)
    text = re.sub(r"semáforo", "semaforo", text)
    text = re.sub(r"ONT NO ENCIENDE / FALLA", "semaforo", text)
    text = re.sub(r"ak", " ", text)
    text = re.sub(r"sglt", "", text)
    text = re.sub(r"bajo cun", "", text)
    text = re.sub(r"cuenta", "", text)
    text = re.sub(r"radica queja el", "", text)
    text = re.sub(r"\xa0justificacion", "", text)
    text = re.sub(r"poruqe", "porque", text)
    text = re.sub(r"cleitne", "cliente", text)
    text = re.sub(r"indciando", "indicando", text)
    text = re.sub(r"swrvicio", "servicio", text)
    text = re.sub(r"instalaon", "instalaron", text)
    text = re.sub(r"medianete", "mediante", text)
    #text = re.sub(r"inf", "informacion", text)


  #####################################################

    text = re.sub(r"nov", "", text)
    #text = re.sub(r"lica", "aplica", text)
               

    #text=re.sub(r'artir', "", text)


    
    text=re.sub(r'redes sociales', "", text)
    text=re.sub(r'informacipon', "informacion", text)
    text=re.sub(r'sur', "", text)
    
    text=re.sub(r'fac turacion', "facturacion", text)
    text=re.sub(r'de conexion', "", text)
    text=re.sub(r'documento', "", text)
    text=re.sub(r'numero', "", text)
    text=re.sub(r'sep', "", text)
    text=re.sub(r'oct', "", text)
    text=re.sub(r'mdmfibra', "", text)
    text=re.sub(r'revchain', "", text)
    text=re.sub(r'mdm', "", text)
    text=re.sub(r'mes', "", text)
    text=re.sub(r'fecbrero', "", text)
    text=re.sub(r'solictando', "solicitando", text)
    
    text=re.sub(r'numero de documento', "", text)
    text=re.sub(r'numero de conexion', "", text)
    text=re.sub(r'numero de cuenta', "", text)

    #######################dirtect tv y hbo max
    text=re.sub(r'directv go', "directv", text)
    text=re.sub(r'directivi go', "directv", text)
    text=re.sub(r'dtv go', "directv", text)
    #text=re.sub(r'paramount', "par", text)
    

    text=re.sub(r'win sports', "winsport", text)
    text=re.sub(r'win sports+', "winsport", text)
    text=re.sub(r'wing sport', "winsport", text)
    text=re.sub(r'win', "winsport", text)

    text=re.sub(r'sva', "svas", text)

    text=re.sub(r'barragan', "", text)





    text=re.sub(r'hbo max', "hbo", text)

    
    text=re.sub(r'omunica', "comunica", text)


    ###esta puede estar sujeta a cambio
    text=re.sub(r'explicacion', "informacion", text)

    text=re.sub(r'lalmda', "llamada", text)
    ########
    text = re.sub(r'\binfo\b', 'informacion', text)
    text = re.sub(r'\binf\b', 'informacion', text)

    text = re.sub(r'informaci', 'informacion', text)
    text = re.sub(r"ntiene", "tiene", text)
    text = re.sub(r"p. m.", "", text)
    

    #numero documento
    #numero de conexion
    #numero de cuenta
    
    text=re.sub(r'deyavargasyahoocom', "", text)




    text = re.sub(r'[-()\"#/@;:<>{}`+=~|.!?,]\|_', "", text)
    text=text.replace("[\'","").replace("\n"," ").replace("']"," ").replace('["',"").replace('"]',"").replace("/","").replace("\', \' ;'","")
    text=text.replace("-","").replace(","," ").replace('.'," ")
    text=text.replace('",'," ").replace("\',","").replace( ":\',","").replace("!","").replace(":","").replace(',"',"")
    text=text.replace("[","").replace("]","").replace("\'s","'s")
    text = text.replace("\'s", "")
    
    text=re.sub(r'rf', "", text)
    text=re.sub(r'\xa0solucion', "", text)
    text=re.sub(r'estoyn', "estoy", text)
    text=re.sub(r'_', "", text)
    
    


    return text