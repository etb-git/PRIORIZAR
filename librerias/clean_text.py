
import pandas as pd
import re

### prueba

print('entro2')
 
def clean_text(text):
    
    text = text.lower()
    
    text=re.sub(r'cliene', "cliente", text)

    #text=re.sub(r".*// cliente", " ", text, flags=re.IGNORECASE)

    #text=re.sub(r".*com", " ", text, flags=re.IGNORECASE)
    #text=re.sub(r".*com", " ", text, flags=re.IGNORECASE)
    

    #text=re.sub(r".*//cliente", " ", text, flags=re.IGNORECASE)
    
    text = re.sub(r"[0-9]", "", text)

    #text = re.sub(r"Motivo de llamada:\s*(.*)", r'\1', text)

   
    #text=re.sub(r'^.*?(MOTIVO:)', r'\1', text)


    #text=re.sub(r'^.*?desea validar\s*',"",text, flags=re.IGNORECASE)

    text=re.sub(r'^.*?se comunica\s*',"",text, flags=re.IGNORECASE)

    text=re.sub(r'^.*?peticion\s*',"",text, flags=re.IGNORECASE)

    text=re.sub(r'^.*?cliente desea\s*',"",text, flags=re.IGNORECASE)


    text=re.sub(r'^.*?cliente requiere\s*',"",text, flags=re.IGNORECASE)
    
    
    #text=re.sub(r'^.*?cuenta de facturacion\s*',"",text, flags=re.IGNORECASE)
    
    
    text=re.sub(r'^.*?cliente se comunica\s*',"",text, flags=re.IGNORECASE)

    text=re.sub(r'^.*?solicitud del cliente\s*',"",text, flags=re.IGNORECASE)
    
    
    #text=re.sub(r'^.*?cuenta\s*',"",text, flags=re.IGNORECASE)

    #text=re.sub(r'^.*?cedula de ciudadania\s*',"",text, flags=re.IGNORECASE)
    #text=re.sub(r'^.*?//cliente\s*',"",text, flags=re.IGNORECASE)

    text=re.sub(r'^.*?aseg//*',"",text, flags=re.IGNORECASE)
   
    text=re.sub(r'^.*?motivo de retiro\s*',"",text, flags=re.IGNORECASE)
    text=re.sub(r'^.*?motivo de llamada\s*',"",text, flags=re.IGNORECASE)
    text=re.sub(r'^.*?motivo de la llamada\s*',"",text, flags=re.IGNORECASE)
    text=re.sub(r'^.*?motivo\s*',"",text, flags=re.IGNORECASE)
    #text=re.sub(r'^.*?llamada:\s*',"",text, flags=re.IGNORECASE)

    text=re.sub(r'^.*?cliente quiere\s*',"",text, flags=re.IGNORECASE)
    





    
    #text=re.sub(r'^.*?el indica*',"",text, flags=re.IGNORECASE)
    
    

    #text=re.sub(r'^.*?ap\s*',"",text, flags=re.IGNORECASE)





    
    #text=re.sub(r'^.*?(ASUNTO:)', r'\1', text)
    #text=re.sub(r'^.*?(descripcion:)', r'\1', text)
    #text=re.sub(r'^.*?(\\ cliente)', r'\1', text)


    #text=re.sub(r'^.*?(FACTURADOS,)', r'\1', text)
    #text=re.sub(r'^.*?(APP MIETB//)', r'\1', text)

    

    #text=re.sub(r'\baseg lt\b', '', text)
    
  


 
    text = re.sub(r"linea", "", text)
    
    text = re.sub(r"LEY 1755", "", text)
    text = re.sub(r"Ley 1755", "", text)
    #text = re.sub(r"ID", "", text)
    
    text = re.sub(r"numeor", "", text)
    text = re.sub(r"MDM-FIBRA-", "", text)

    #text=re.sub(r'^.*?de la llamada\s*', "", text)


    
   
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
   

    text = re.sub(r"reset", "reiniciar", text)
    text = re.sub(r"arear", "area", text)
    text = re.sub(r"tegnicas", "tecnicas", text)
    
  
    text = re.sub(r"reiniciarr", "reiniciar", text)
    text = re.sub(r"celular", "", text)
    text = re.sub(r"servicios", "servicio", text)
    text = re.sub(r"wifi", "wiffi", text)
    text = re.sub(r"kr", " ", text)
    text = re.sub(r"validan", "valida", text)
   
    #text = re.sub(r"go", "directvgo", text)
    text = re.sub(r"agendamiento", "agenda", text)
    text = re.sub(r"moden", "modem", text)

    
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

    text=re.sub(r'comun ica', "comunica", text)



    text=re.sub(r'hbo max', "hbo", text)

    
    text=re.sub(r'omunica', "comunica", text)


    ###esta puede estar sujeta a cambio
    text=re.sub(r'explicacion', "informacion", text)

    text=re.sub(r'lalmda', "llamada", text)
    ########
    text = re.sub(r'\binfo\b', 'informacion', text)
    text = re.sub(r'\binf\b', 'informacion', text)
    text = re.sub(r'\bfac\b', 'factura', text)
    #text = re.sub(r'informaci', 'informacion', text)
    text = re.sub(r"ntiene", "tiene", text)
    text = re.sub(r"p. m.", "", text)

    text = re.sub(r"in formacion", "informacion", text)
    text = re.sub(r"informes", "informacion", text)
    
    text = re.sub(r"por que", "porque", text)
    text = re.sub(r"ley", "", text)

    text = re.sub(r"por que", "porque", text)
    text = re.sub(r"actulaizacionde", "actualizacion", text)
    
    text = re.sub(r"paramot", "paramount", text)
    

    #text = re.sub(r"d ela", "de la", text)

    #numero documento
    #numero de conexion
    #numero de cuenta
    
    text=re.sub(r'%', "", text)
   



    text = re.sub(r'[-()\"#/@;:%<>+{}`+=~|.!?,]\|_', "", text)
    text=text.replace("[\'","").replace("\n"," ").replace("']"," ").replace('["',"").replace('"]',"").replace("/","").replace("\', \' ;'","")
    text=text.replace("-","").replace(","," ").replace('.'," ").replace('+',"").replace('('," ").replace(')'," ")
    text=text.replace('",'," ").replace("\',","").replace( ":\',","").replace("!","").replace(":","").replace(',"',"")
    text=text.replace("[","").replace("]","").replace("\'s","'s")
    text = text.replace("\'s", "")
    
    text=re.sub(r'rf', "", text)
    text=re.sub(r'\xa0solucion', "", text)
    text=re.sub(r'estoyn', "estoy", text)
    text=re.sub(r'_', "", text)
    
    text = re.sub(r"correo", "", text)
    text = re.sub(r"\S+@\S+\s+\S+", "", text)

    text = re.sub(r'"', '', text)

    text = re.sub(r'x', 'por', text)

    


    return text