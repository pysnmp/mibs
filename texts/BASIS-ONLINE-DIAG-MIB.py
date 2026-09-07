#
# PySNMP MIB module BASIS-ONLINE-DIAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source BASIS-ONLINE-DIAG-MIB
# Source digest sha256:34235012a13c73c28793c5b7b03bf37dd78b1fcc15f6539ada1db302031a19b7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
axisDiagnostics, = mibBuilder.importSymbols("BASIS-MIB", "axisDiagnostics")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
basisOnlineDiagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 80))
basisOnlineDiagMIB.setRevisions(('2003-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: basisOnlineDiagMIB.setRevisionsDescriptions(('Initial version of the MIB.\n\n        The content of this MIB was originally available\n        in CISCO-WAN-AXIPOP-MIB defined using SMIv1.\n        The applicable objects from CISCO-WAN-AXIPOP-MIB\n        are defined using SMIv2 in this MIB. Also the\n        descriptions of some of the objects have been \n        modified.',))
if mibBuilder.loadTexts: basisOnlineDiagMIB.setLastUpdated('2003-06-11 00:00')
if mibBuilder.loadTexts: basisOnlineDiagMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: basisOnlineDiagMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: basisOnlineDiagMIB.setDescription('This MIB contains information on the online diagnostics\n        in MGX82xx(MGX8250, MGX8220, MGX8230 etc) products.')
onlineDiagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 6, 3))
diagType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("post", 1), ("onlinediag", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagType.setStatus('current')
if mibBuilder.loadTexts: diagType.setDescription('This is used to identify the type of diagnostics.\n\n        post (1)      : Power On Self Test.\n        onlineDiag(2) : Online Diagnostics. \n\n        When a trap is sent to report diagnostics results\n        this is used as a varbind to indicate the type of \n        diagnostics.')
diagResult = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("passed", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagResult.setStatus('current')
if mibBuilder.loadTexts: diagResult.setDescription('This is used to indicate the result of the diagnostics.')
diagTestId = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 6, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diagTestId.setStatus('current')
if mibBuilder.loadTexts: diagTestId.setDescription('This is used to indicate the test number of the\n        diagnostics test that failed. The value depends upon\n        the implementation in the each of the MGX82xx product.')
boDiagMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2))
boDiagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1))
boDiagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2))
boDiagCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 1, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "boDiagGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagCompliance = boDiagCompliance.setStatus('current')
if mibBuilder.loadTexts: boDiagCompliance.setDescription('The compliance statement for entities which implement\n        the basis online diagnostics MIB.')
boDiagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 80, 2, 2, 1)).setObjects(("BASIS-ONLINE-DIAG-MIB", "diagType"), ("BASIS-ONLINE-DIAG-MIB", "diagResult"), ("BASIS-ONLINE-DIAG-MIB", "diagTestId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    boDiagGroup = boDiagGroup.setStatus('current')
if mibBuilder.loadTexts: boDiagGroup.setDescription('A collection of objects providing the\n         online diagnostics information.')
mibBuilder.exportSymbols("BASIS-ONLINE-DIAG-MIB", PYSNMP_MODULE_ID=basisOnlineDiagMIB, basisOnlineDiagMIB=basisOnlineDiagMIB, boDiagCompliance=boDiagCompliance, boDiagGroup=boDiagGroup, boDiagMIBCompliances=boDiagMIBCompliances, boDiagMIBConformance=boDiagMIBConformance, boDiagMIBGroups=boDiagMIBGroups, diagResult=diagResult, diagTestId=diagTestId, diagType=diagType, onlineDiagnostics=onlineDiagnostics)
