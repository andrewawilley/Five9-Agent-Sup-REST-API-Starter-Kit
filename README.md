# Overview

This is a work-in-progress "how to" with some examples of using the Five9 Agetn and Supervisor REST API endpoints.  

There are two main documents.  The first (agent_sup_VCC_boilerplate.html) is the most useful in demonstrating individual sample functionality.  It can be opened in the same browser as an active Agent session and provides links on the left-hand side that perform some of the most commonly implemented API actions.

The second (agent_sup_VCC_boilerplage with sockets.html) is a less-fleshed-out functional demonstration page, but shows how you can better leverage the Five9 event socket and attach listeners to events that you may want to react to.  

## Using the Five9 Agent/Supervisor REST API 

As described in the <a href="https://webapps.five9.com/assets/files/for_customers/documentation/apis/vcc-agent+supervisor-rest-api-reference-guide.pdf">documentation</a>, using the VCC REST API endpoints follows this pattern

* Obtain session metadata from [https://app.five9.com/appsvcs/rs/svc/auth/metadata](https://app.five9.com/appsvcs/rs/svc/auth/metadata)
* Build the base api url (API domain:port)
* Determine the appropriate context path for the endpoint
* Invoke the method with the fully formed path

# DISCLAIMER

This repository contains sample code which is **not an official Five9 resource**. It's intended for educational and illustrative purposes only, demonstrating potential ways to utilize APIs in the Five9 contact center environment.

Under the MIT License:

- This is **not** officially endorsed or supported software by Five9.
- All customizations, modifications, or deployments made with this code are entirely at your **own risk** and **responsibility**.
- The provided code may not cover all possible use cases or be adapted to your specific needs without further modification.
- Five9 will **not** provide any support or assume any liability for any issues that may arise from the use of this code.

For a fully supported, robust, and tailor-made solution, we highly recommend consulting with Five9's professional services team and TAM teams.

