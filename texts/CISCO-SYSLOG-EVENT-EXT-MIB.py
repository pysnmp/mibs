#
# PySNMP MIB module CISCO-SYSLOG-EVENT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SYSLOG-EVENT-EXT-MIB
# Source digest sha256:a1e4d6abc77cf132383eb00b35f5df3937eedcc1af05b8a6feee612905e35b3a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SyslogSeverity, = mibBuilder.importSymbols("CISCO-SYSLOG-MIB", "SyslogSeverity")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSyslogEventExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 270))
ciscoSyslogEventExtMIB.setRevisions(('2002-02-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setLastUpdated('2002-02-12 00:00')
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive,\n                        San Jose CA 95134-1706.\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSyslogEventExtMIB.setDescription('This MIB module extends the Cisco Syslog \n                MIB and provides network management support \n                to handle and process Syslog messages as \n                device events.')
ciscoSyslogEventExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 1))
cslogEventConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1))
class CslogEventDisposition(TextualConvention, Bits):
    description = 'This definition specifies the manner in which a \n                Syslog message should be handled by the system as \n                a device event. Events are first recorded by the \n                Syslog subsystem, and then they can be counted, \n                displayed on the console, or forward to external \n                device. The four disposition mechanisms are:\n                    none(0)     - Record only, no further handling. \n                    count(1)    - All Syslog messages received after\n                                  this bit is set will be counted \n                                  according to their corresponding \n                                  event types.  \n                    display(2)  - All Syslog messages received after\n                                  this bit is set will be displayed on \n                                  the device console, HTML console \n                                  or WEB pages (pending on severity \n                                  level configuration of each display \n                                  types).\n                    notify(3)   - All Syslog messages received after\n                                  this bit is set will cause \n                                  notification to be sent.'
    status = 'current'
    namedValues = NamedValues(("none", 0), ("count", 1), ("display", 2), ("notify", 3))

cslogEventDetailDefault = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noDisplay", 1), ("sparseDetail", 2), ("normalDetail", 3), ("verboseDetail", 4), ("exhaustiveDetail", 5))).clone('normalDetail')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventDetailDefault.setStatus('current')
if mibBuilder.loadTexts: cslogEventDetailDefault.setDescription('This object defines the detail level at which\n                Syslog messages are displayed on the console or \n                HTML user interface. Detail level classifications \n                are:\n                    noDisplay(1)         - No display at all.\n                    sparseDetail(2)      - Minimum detail.\n                    normalDetail(3)      - General detail.\n                    verboseDetail(4)     - Verbose detail.\n                    exhaustiveDetail(5)  - Full detail.')
cslogEventSeverityDispConsole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 2), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispConsole.setStatus('current')
if mibBuilder.loadTexts: cslogEventSeverityDispConsole.setDescription('This object indicates which syslog severity \n                level messages can be displayed on the console. \n                A high severity value implies a low severity.\n                If the display bit on the object \n                cslogEventDisposition is set for this severity, \n                all messages have severity values less than or \n                equal to clogMaxSeverity and this object will \n                be displayed on the console.')
cslogEventSeverityDispHtmlGUI = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 3), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlGUI.setStatus('current')
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlGUI.setDescription('This object indicates which syslog severity \n                level messages can be displayed on the event log \n                GUI. A high severity value implies a low severity.\n                If the display bit on the object \n                cslogEventDisposition is set for this severity, \n                all messages have severity values less than or \n                equal to clogMaxSeverity and this object will \n                be displayed on the event log GUI web pages.')
cslogEventSeverityDispHtmlConsol = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 4), SyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlConsol.setStatus('current')
if mibBuilder.loadTexts: cslogEventSeverityDispHtmlConsol.setDescription('This object indicates which syslog severity \n                level messages can be displayed on the HTML \n                event log console. \n                A high severity value implies a low severity.\n                If the display bit on the object \n                cslogEventDisposition is set for this severity, \n                all messages have severity values less than or \n                equal to clogMaxSeverity and this object will \n                be displayed on the GUI browser console page.')
cslogEventDispositionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cslogEventDispositionTable.setStatus('current')
if mibBuilder.loadTexts: cslogEventDispositionTable.setDescription('This table contains parameters to configure \n                Syslog message disposition mechanisms and keep\n                message counts.')
cslogEventDispositionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionSeverity"))
if mibBuilder.loadTexts: cslogEventDispositionEntry.setStatus('current')
if mibBuilder.loadTexts: cslogEventDispositionEntry.setDescription('There is one entry per Syslog severity in the\n                cslogEventDispositionTable. Each entry contains \n                parameters for message disposition and count.')
cslogEventDispositionSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 1), SyslogSeverity()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cslogEventDispositionSeverity.setStatus('current')
if mibBuilder.loadTexts: cslogEventDispositionSeverity.setDescription('This object defines the Syslog serverity.')
cslogEventDisposition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 2), CslogEventDisposition().clone(('none',))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslogEventDisposition.setStatus('current')
if mibBuilder.loadTexts: cslogEventDisposition.setDescription('This object defines the disposition method for \n                Syslog messages of a specific severity.')
cslogEventDispositionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 270, 1, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslogEventDispositionCount.setStatus('current')
if mibBuilder.loadTexts: cslogEventDispositionCount.setDescription('This is the number of Syslog messages of a specific\n                severity.')
ciscoSlogEventExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2))
ciscoSlogEventExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1))
ciscoSlogEventExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2))
ciscoSlogEventExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 1, 1)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "ciscoSlogEventExtConfigGroup"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "ciscoSlogEventExtStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtCompliance = ciscoSlogEventExtCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSlogEventExtCompliance.setDescription('The compliance statement for the cslogEventExt \n                groups.')
ciscoSlogEventExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 1)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDetailDefault"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispConsole"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlGUI"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventSeverityDispHtmlConsol"), ("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDisposition"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtConfigGroup = ciscoSlogEventExtConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSlogEventExtConfigGroup.setDescription('These are objects supporting Syslog event \n                configuration.')
ciscoSlogEventExtStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 270, 2, 2, 2)).setObjects(("CISCO-SYSLOG-EVENT-EXT-MIB", "cslogEventDispositionCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlogEventExtStatsGroup = ciscoSlogEventExtStatsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSlogEventExtStatsGroup.setDescription('These are objects to provide Syslog event \n                statistics.')
mibBuilder.exportSymbols("CISCO-SYSLOG-EVENT-EXT-MIB", CslogEventDisposition=CslogEventDisposition, PYSNMP_MODULE_ID=ciscoSyslogEventExtMIB, ciscoSlogEventExtCompliance=ciscoSlogEventExtCompliance, ciscoSlogEventExtConfigGroup=ciscoSlogEventExtConfigGroup, ciscoSlogEventExtMIBCompliances=ciscoSlogEventExtMIBCompliances, ciscoSlogEventExtMIBConformance=ciscoSlogEventExtMIBConformance, ciscoSlogEventExtMIBGroups=ciscoSlogEventExtMIBGroups, ciscoSlogEventExtStatsGroup=ciscoSlogEventExtStatsGroup, ciscoSyslogEventExtMIB=ciscoSyslogEventExtMIB, ciscoSyslogEventExtMIBObjects=ciscoSyslogEventExtMIBObjects, cslogEventConfig=cslogEventConfig, cslogEventDetailDefault=cslogEventDetailDefault, cslogEventDisposition=cslogEventDisposition, cslogEventDispositionCount=cslogEventDispositionCount, cslogEventDispositionEntry=cslogEventDispositionEntry, cslogEventDispositionSeverity=cslogEventDispositionSeverity, cslogEventDispositionTable=cslogEventDispositionTable, cslogEventSeverityDispConsole=cslogEventSeverityDispConsole, cslogEventSeverityDispHtmlConsol=cslogEventSeverityDispHtmlConsol, cslogEventSeverityDispHtmlGUI=cslogEventSeverityDispHtmlGUI)
