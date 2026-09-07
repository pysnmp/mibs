#
# PySNMP MIB module CISCO-ATM-SWITCH-ADDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-SWITCH-ADDR-MIB
# Source digest sha256:24032e0e242379c20e945d0430b801f40aebe9d278867f9c22c05d5536e912dd
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoAtmSwAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 51))
ciscoAtmSwAddrMIB.setRevisions(('1996-01-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setLastUpdated('1996-01-10 00:00')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setContactInfo('       Cisco Systems\n\t\t\tCustomer Service\n\n\t\tPostal: 170 W Tasman Drive\n\t\t\tSan Jose, CA  95134\n\t\t\tUSA\n\n\t\t   Tel: +1 800 553-NETS\n\n\t\tE-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setDescription('ATM Switch address MIB')
ciscoAtmSwAddrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 1))
class AtmAddr(TextualConvention, OctetString):
    description = 'The ATM address used by the network entity.  The\n\t\taddress types are: network prefix (13 octets), and NSAP (20\n\t\toctets).'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
ciscoAtmSwAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoAtmSwAddrTable.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrTable.setDescription('This table contains an address list on a per switch\n                 basis.')
ciscoAtmSwAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrIndex"))
if mibBuilder.loadTexts: ciscoAtmSwAddrEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrEntry.setDescription('An entry in the ciscoAtmSwAddrTable.')
ciscoAtmSwAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoAtmSwAddrIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrIndex.setDescription('A sequence number when address gets created.\n\t\t  1 is the primary address. This is dense table and\n\t\t  this index will be re-sequenced when a entry get\n\t\t  deleted and it can only create new entry when append\n\t\t  in the end of table.')
ciscoAtmSwAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 2), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoAtmSwAddrAddress.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrAddress.setDescription('A valid address for a given switch.')
ciscoAtmSwAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoAtmSwAddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrRowStatus.setDescription('This object is used to create and delete rows in the\n                 ciscoAtmSwAddrTable.')
ciscoAtmSwAddrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3))
ciscoAtmSwAddrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1))
ciscoAtmSwAddrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2))
ciscoAtmSwAddrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmSwAddrMIBCompliance = ciscoAtmSwAddrMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIBCompliance.setDescription('The compliance statement for the Cisco ATM switch address\n             group.')
ciscoAtmSwAddrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2, 1)).setObjects(("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrAddress"), ("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmSwAddrMIBGroup = ciscoAtmSwAddrMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIBGroup.setDescription('')
mibBuilder.exportSymbols("CISCO-ATM-SWITCH-ADDR-MIB", AtmAddr=AtmAddr, PYSNMP_MODULE_ID=ciscoAtmSwAddrMIB, ciscoAtmSwAddrAddress=ciscoAtmSwAddrAddress, ciscoAtmSwAddrEntry=ciscoAtmSwAddrEntry, ciscoAtmSwAddrIndex=ciscoAtmSwAddrIndex, ciscoAtmSwAddrMIB=ciscoAtmSwAddrMIB, ciscoAtmSwAddrMIBCompliance=ciscoAtmSwAddrMIBCompliance, ciscoAtmSwAddrMIBCompliances=ciscoAtmSwAddrMIBCompliances, ciscoAtmSwAddrMIBConformance=ciscoAtmSwAddrMIBConformance, ciscoAtmSwAddrMIBGroup=ciscoAtmSwAddrMIBGroup, ciscoAtmSwAddrMIBGroups=ciscoAtmSwAddrMIBGroups, ciscoAtmSwAddrMIBObjects=ciscoAtmSwAddrMIBObjects, ciscoAtmSwAddrRowStatus=ciscoAtmSwAddrRowStatus, ciscoAtmSwAddrTable=ciscoAtmSwAddrTable)
