#
# PySNMP MIB module CISCO-ATM-SERVICE-REGISTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-SERVICE-REGISTRY-MIB
# Source digest sha256:897e694926dcf4158d0c9b0d0bdac39ebd1bef7e2de44412e14a11d18326a1b7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoAtmServiceRegistryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 50))
ciscoAtmServiceRegistryMIB.setRevisions(('1996-02-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setLastUpdated('1996-02-21 00:00')
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134-1706\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setDescription("A MIB module to allow an NMS to monitor and\n                configure the information which an ATM switch\n                makes available via the ILMI's Service Registry\n                Table.")
ciscoAtmServiceRegistryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 1))
class AtmAddr(TextualConvention, OctetString):
    description = 'The ATM address used by the network entity.  The\n            address types are: no address (0 octets), E.164 (8\n            octets), network prefix (13 octets), and NSAP (20\n            octets).  Note: The E.164 address is encoded in\n            BCD format.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
class InterfaceIndexOrZero(TextualConvention, Integer32):
    description = 'Either the value 0, or the ifIndex value of an\n            ATM Interface.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

asrSrvcRegTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: asrSrvcRegTable.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegTable.setDescription('The table implemented by an ATM switch to allow\n                monitoring and control of the ATM addresses of\n                registered services which it makes avaiable to ATM\n                end-systems via the ILMI across its UNIs.')
asrSrvcRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegPort"), (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegServiceID"), (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegAddressIndex"))
if mibBuilder.loadTexts: asrSrvcRegEntry.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegEntry.setDescription('Information about a single service provider that is \n                to be made available to the user-side of one or more\n                ATM UNIs.  An entry, for which asrSrvcRegPort has a\n                non-zero value, is a specific assignment to that UNI;\n                an entry for which asrSrvcRegPort is zero applies to\n                all UNIs for which this table contains no specific\n                assignments.')
asrSrvcRegPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: asrSrvcRegPort.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegPort.setDescription('Either the value 0, or the ifIndex value of an\n                the ATM Interface.  A row for which this object has a\n                non-zero value is a specific assignment to that UNI;\n                a row for which this object is zero applies to\n                all UNIs for which this table contains no specific\n                assignments.\n\n                Some switches may only support this object with the\n                value of zero.')
asrSrvcRegServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: asrSrvcRegServiceID.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegServiceID.setDescription('The service identifier which uniquely identifies\n                the type of service at the address given by the\n                corresponding value of asrSrvcRegATMAddress.\n\n                Specific values for this identifier are defined in\n                the ILMI specification (e.g., asrSrvcRegLecs) or\n                elsewhere.')
asrSrvcRegATMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 3), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegATMAddress.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegATMAddress.setDescription('An ATM address to which the ATM end-system on this\n                UNI can attempt to establish a connection for the\n                service.')
asrSrvcRegAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 4), Integer32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: asrSrvcRegAddressIndex.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegAddressIndex.setDescription('An arbitrary integer to differentiate multiple rows\n                containing different ATM addresses for the same service\n                on the same UNI.')
asrSrvcRegParm1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegParm1.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegParm1.setDescription('An octet string used according to the value of \n                asrSrvcRegServiceID.')
asrSrvcRegRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegRowStatus.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegRowStatus.setDescription("The status of this row.  No object in the row can\n                be modified while the value of this object is\n                'active'.")
asrSrvcRegMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3))
asrSrvcRegMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1))
asrSrvcRegMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2))
asrSrvcRegMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1, 1)).setObjects(("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asrSrvcRegMIBCompliance = asrSrvcRegMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegMIBCompliance.setDescription('The compliance statement for ATM switches which\n                implement the Cisco Service Registry MIB')
asrSrvcRegMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2, 1)).setObjects(("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegATMAddress"), ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegParm1"), ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asrSrvcRegMIBGroup = asrSrvcRegMIBGroup.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegMIBGroup.setDescription('A collection of objects providing monitoring and\n                control of ATM addresses of services which an ATM\n                switch is to make available via the ILMI.')
mibBuilder.exportSymbols("CISCO-ATM-SERVICE-REGISTRY-MIB", AtmAddr=AtmAddr, InterfaceIndexOrZero=InterfaceIndexOrZero, PYSNMP_MODULE_ID=ciscoAtmServiceRegistryMIB, asrSrvcRegATMAddress=asrSrvcRegATMAddress, asrSrvcRegAddressIndex=asrSrvcRegAddressIndex, asrSrvcRegEntry=asrSrvcRegEntry, asrSrvcRegMIBCompliance=asrSrvcRegMIBCompliance, asrSrvcRegMIBCompliances=asrSrvcRegMIBCompliances, asrSrvcRegMIBConformance=asrSrvcRegMIBConformance, asrSrvcRegMIBGroup=asrSrvcRegMIBGroup, asrSrvcRegMIBGroups=asrSrvcRegMIBGroups, asrSrvcRegParm1=asrSrvcRegParm1, asrSrvcRegPort=asrSrvcRegPort, asrSrvcRegRowStatus=asrSrvcRegRowStatus, asrSrvcRegServiceID=asrSrvcRegServiceID, asrSrvcRegTable=asrSrvcRegTable, ciscoAtmServiceRegistryMIB=ciscoAtmServiceRegistryMIB, ciscoAtmServiceRegistryMIBObjects=ciscoAtmServiceRegistryMIBObjects)
