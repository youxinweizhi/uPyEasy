# Autogenerated file
def render(info, nodes):
    yield """      <form>
         <table>
            <TR>
               <TH>System Info
               <TH>Value
               <TH>
               <TH>System Info
               <TH>Value
               <TH>
            <TR>
               <TD>Unit:
               <TD>"""
    yield str(info['unit'])
    yield """
               <TD>
               <TD>uPyEasy version:
               <TD>"""
    yield str(info['version'])
    yield """
            <TR>
               <TD>Local Time:
               <TD>"""
    yield str(info['time'])
    yield """
               <TD>
               <TD>Platform:
               <TD>"""
    yield str(info['platform'])
    yield """
            <TR>
               <TD>Uptime:
               <TD>"""
    yield str(info['uptime'])
    yield """
               <TD>
               <TD>Free/Total Heap:
               <TD>"""
    yield str(info['heap'])
    yield """
            <TR>
               <TD>IP:
               <TD>"""
    yield str(info['ip'])
    yield """
               <TD>
               <TD>Used Stack Mem:
               <TD>"""
    yield str(info['stack'])
    yield """
            <TR>
               <TH>Node List:
               <TH>Name
               <TH>Build
               <TH>Type
               <TH>IP
               <TH>Age
        """
    for node in nodes:
        yield """            <TR>
               <TD>
               <TD>
               <TD>
               <TD>
               <TD>
        """
    yield """            <TR>
               <TD colspan='2'>
                  <hr>
            <TR>
               <TD>
               <TD>
         </table>
      </form>
"""
