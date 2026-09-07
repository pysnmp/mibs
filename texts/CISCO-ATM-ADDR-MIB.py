#
# PySNMP MIB module CISCO-ATM-ADDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-ADDR-MIB
# Source digest sha256:b4673c2831aab055852bfdb4c964057deb9a0551ad7f36ee7e9c48d4d3fdb12e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoAtmAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 12))
ciscoAtmAddrMIB.setRevisions(('1996-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmAddrMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setLastUpdated('1996-05-06 00:00')
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setContactInfo('       Cisco Systems\n\t\t\tCustomer Service\n\n\t\tPostal: 170 W Tasman Drive\n\t\t\tSan Jose, CA  95134\n\t\t\tUSA\n\n\t\t   Tel: +1 800 553-NETS\n\n\t\tE-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setDescription('ATM address MIB')
class AtmAddr(TextualConvention, OctetString):
    description = 'The ATM address used by the network entity.  The\n\t\taddress types are: no address (0 octets), E.164 (8\n\t\toctets), network prefix (13 octets), and NSAP (20\n\t\toctets).  Note: The E.164 address is encoded in\n\t\tBCD format.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
ciscoAtmAddrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 1))
ciscoAtmIfAdminAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrTable.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrTable.setDescription('This table contains an address list on a per interface\n                 basis.  This table only applies to switches or networks\n                 and only for interfaces that have more than one address\n                 assigned.')
ciscoAtmIfAdminAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrAddress"))
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrEntry.setDescription('An entry in the CiscoAtmIfAdminAddrTable.')
ciscoAtmIfAdminAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 1), AtmAddr()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrAddress.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrAddress.setDescription('A valid address for a given switch or network\n                 interface.')
ciscoAtmIfAdminAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrRowStatus.setDescription('This object is used to create and delete rows in the\n                 atmIfAdminAddrTable.')
ciscoAtmIfAdminAddrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3))
ciscoAtmIfAdminAddrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1))
ciscoAtmIfAdminAddrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2))
ciscoAtmIfAdminAddrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1, 1)).setObjects(("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfAdminAddrMIBCompliance = ciscoAtmIfAdminAddrMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrMIBCompliance.setDescription('The compliance statement for the Cisco ATM address\n                   group.')
ciscoAtmIfAdminAddrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2, 1)).setObjects(("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfAdminAddrMIBGroup = ciscoAtmIfAdminAddrMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrMIBGroup.setDescription('This object is used to create and delete rows in the\n                   atmIfAdminAddrTable.')
mibBuilder.exportSymbols("CISCO-ATM-ADDR-MIB", AtmAddr=AtmAddr, PYSNMP_MODULE_ID=ciscoAtmAddrMIB, ciscoAtmAddrMIB=ciscoAtmAddrMIB, ciscoAtmAddrMIBObjects=ciscoAtmAddrMIBObjects, ciscoAtmIfAdminAddrAddress=ciscoAtmIfAdminAddrAddress, ciscoAtmIfAdminAddrEntry=ciscoAtmIfAdminAddrEntry, ciscoAtmIfAdminAddrMIBCompliance=ciscoAtmIfAdminAddrMIBCompliance, ciscoAtmIfAdminAddrMIBCompliances=ciscoAtmIfAdminAddrMIBCompliances, ciscoAtmIfAdminAddrMIBConformance=ciscoAtmIfAdminAddrMIBConformance, ciscoAtmIfAdminAddrMIBGroup=ciscoAtmIfAdminAddrMIBGroup, ciscoAtmIfAdminAddrMIBGroups=ciscoAtmIfAdminAddrMIBGroups, ciscoAtmIfAdminAddrRowStatus=ciscoAtmIfAdminAddrRowStatus, ciscoAtmIfAdminAddrTable=ciscoAtmIfAdminAddrTable)
