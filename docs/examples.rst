.. _examples:

=====================
Ready-to-Run Examples
=====================

This page contains examples for OpenLEADR:

.. _client_example:

Client Example
==============

This example sets up a minimal OpenADR Client (Virtual End Node):

.. code-block:: python3

    from openleadr import OpenADRClient
    import asyncio

    async def main():
        client = OpenADRClient(ven_name="Device001", vtn_url="http://localhost:8080/OpenADR2/Simple/2.0b")
        client.on_event = handle_event
        await client.run()

    async def handle_event(event):
        """
        This coroutine will be called
        whenever there is an event to be handled.
        """
        print("There is an event!")
        print(event)
        return 'optIn'

    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()




.. _server_example:

Server Example
==============

.. _server_with_gui_example:

Server with GUI Example
=======================