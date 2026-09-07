#
# PySNMP MIB module ALTIGA-IP-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALTIGA-IP-STATS-MIB
# Source digest sha256:5114c13dc62fa3aad22f9ad19987cce8651c942349fc9a34ff6aaaa66dc386c6
# Produced by pysmi-2.3.0
#
alIpMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alIpMibModule")
alIpGroup, alStatsIp = mibBuilder.importSymbols("ALTIGA-MIB", "alIpGroup", "alStatsIp")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaIpStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2))
altigaIpStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaIpStatsMibModule.setRevisionsDescriptions(('Added module compliance.', 'Updated with new header',))
if mibBuilder.loadTexts: altigaIpStatsMibModule.setLastUpdated('2002-09-05 13:00')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setContactInfo('Cisco Systems\n          170 W Tasman Drive\n          San Jose, CA  95134\n          USA\n\n          Tel: +1 800 553-NETS\n          E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaIpStatsMibModule.setDescription('The Altiga IP Statistics MIB models counters and objects that are\n          of management interest for IP.\n         \n          Acronyms\n          The following acronyms are used in this document:\n\n            IP:         Internet Protocol\n\n            LAN:        Local-Area Network \n\n            MIB:        Management Information Base\n\n         ')
alStatsIpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1))
alIpInterfaceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alIpInterfaceStatsTable.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsTable.setDescription('IP Interface Statistics table.')
alIpInterfaceStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"))
if mibBuilder.loadTexts: alIpInterfaceStatsEntry.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsEntry.setDescription('An entry in the alIpInterfaceStatsTable.')
alIpInterfaceStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alIpInterfaceStatsIndex.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsIndex.setDescription('The ifIndex of this row.')
alIpInterfaceStatsCurrentDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("full", 2), ("half", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alIpInterfaceStatsCurrentDuplex.setStatus('current')
if mibBuilder.loadTexts: alIpInterfaceStatsCurrentDuplex.setDescription('The current LAN duplex mode for this interface.')
altigaIpStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1))
altigaIpStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1))
altigaIpStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 13, 2, 1, 1, 1)).setObjects(("ALTIGA-IP-STATS-MIB", "altigaIpStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaIpStatsMibCompliance = altigaIpStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaIpStatsMibCompliance.setDescription('The compliance statement for agents which \n       implement the Altiga IP Statistics MIB.')
altigaIpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 8, 2)).setObjects(("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsIndex"), ("ALTIGA-IP-STATS-MIB", "alIpInterfaceStatsCurrentDuplex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaIpStatsGroup = altigaIpStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaIpStatsGroup.setDescription('The objects for Ip Statistics.')
mibBuilder.exportSymbols("ALTIGA-IP-STATS-MIB", PYSNMP_MODULE_ID=altigaIpStatsMibModule, alIpInterfaceStatsCurrentDuplex=alIpInterfaceStatsCurrentDuplex, alIpInterfaceStatsEntry=alIpInterfaceStatsEntry, alIpInterfaceStatsIndex=alIpInterfaceStatsIndex, alIpInterfaceStatsTable=alIpInterfaceStatsTable, alStatsIpGlobal=alStatsIpGlobal, altigaIpStatsGroup=altigaIpStatsGroup, altigaIpStatsMibCompliance=altigaIpStatsMibCompliance, altigaIpStatsMibCompliances=altigaIpStatsMibCompliances, altigaIpStatsMibConformance=altigaIpStatsMibConformance, altigaIpStatsMibModule=altigaIpStatsMibModule)
