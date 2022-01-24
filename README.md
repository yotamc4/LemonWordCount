# LemonWordCount

### Installation:
  1. Clone this project.
  2. From terminal (with root directory set to 'WordStatisticsApi') run 
> python Installation.py 

(this will install required packages using pip).

### Run the API:
  From terminal (with root directory set to '..\WordStatisticsApi') run 
  > python sources/Endpoint.py 

or
  > python sources/Endpoint.py <*explicit port*> <*explicit host*> 
  
  default port and host are 5000 and localhost.

## Word Counter EP:
#### Request:
POST request:
> http://<*host*>:<*port*>/word_counter
> 
> Headers: 'Content-Type:application/json'
> 
> Body: {"type":"<*type*>", "data":"<*url/path/text*>"} 
  
where:
- for type "file" data should be a path to a file.
- for type "text" data should contain the text to be processed.
- for type "url" data should be a valid url.
  
  For example: {"type":"text", "data":"Will the real Slim Shady please stand up?"}
  
#### Response:
application/json format with a suiting http status code and optionally a relevant response message.
  
## Word Statistics EP:
#### Request:
GET request:
> http://<*host*>:<*port*>/word_statistics
>
> headers: 'Content-Type:application/json'
> 
> Body: {"word":"<*word to get statistics for*>"}

For example: {"word":"slim"}

#### Response:
application/json format body {"count": <*number of times input word appeared so far*>}, 
together with a suiting http status code.
