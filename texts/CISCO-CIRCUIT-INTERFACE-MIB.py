#
# PySNMP MIB module CISCO-CIRCUIT-INTERFACE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CIRCUIT-INTERFACE-MIB
# Source digest sha256:56a72f4ae06494b3871056a772d823dd9a946ef17636f9ebcd00bb3eb7567316
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoCircuitInterfaceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 160))
ciscoCircuitInterfaceMIB.setRevisions(('2000-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setLastUpdated('2000-05-09 00:00')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA 95134\n                        USA\n\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIB.setDescription('The MIB module to configure the circuit description\n                for an interface.\n                The circuit description can be used to describe and\n                identify circuits on interfaces like ATM,\n                frame-relay etc.')
ciscoCircuitInterfaceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 1))
cciDescription = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1))
cciDescriptionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cciDescriptionTable.setStatus('current')
if mibBuilder.loadTexts: cciDescriptionTable.setDescription('This table contains a circuit description to identify\n                circuit based interfaces like ATM, Frame-Relay etc.\n                The circuit description could be used for example, to\n                correlate performance statistics associated with the\n                corresponding interfaces.')
cciDescriptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cciDescriptionEntry.setStatus('current')
if mibBuilder.loadTexts: cciDescriptionEntry.setDescription('Each cciDescriptionEntry contains the circuit\n                description for a particular circuit based interface.\n                The entry is identified by the ifIndex which would\n                typically correspond to circuit based interfaces.\n                Interfaces with ifType equal to atm(37),\n                frameRelay(32) frameRelayService(44) are some\n                examples.\n\n                Entries can only be created by management station\n                action.\n                Entries can be deleted by setting the cciStatus object\n                to destroy(6). The agent will delete any cciEntry if\n                the corresponding ifEntry is deleted.\n                Entries are not maintained in any kind of NV-storage,\n                and will not be recreated by the agent after a reboot.')
cciDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cciDescr.setStatus('current')
if mibBuilder.loadTexts: cciDescr.setDescription('The circuit description of the interface. It has no\n                default value.')
cciStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 160, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cciStatus.setStatus('current')
if mibBuilder.loadTexts: cciStatus.setDescription('The row status object, but with restricted values.\n                Only two values are allowed for this object:\n                createAndGo(4) and destroy(6).\n                The row is created by specifying the value for\n                cciDescr and setting this object to createAndGo(4).\n                If the row creation is succesfull, the cciStatus\n                would be active(1). In the active(1) state, the\n                cciDescr can be modifed.\n                The row is deleted by setting this object to\n                destroy(6).')
ciscoCircuitInterfaceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3))
ciscoCircuitInterfaceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1))
ciscoCircuitInterfaceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2))
ciscoCircuitInterfaceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 1, 1)).setObjects(("CISCO-CIRCUIT-INTERFACE-MIB", "ciscoCircuitInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCircuitInterfaceMIBCompliance = ciscoCircuitInterfaceMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCircuitInterfaceMIBCompliance.setDescription('The compliance statement for Cisco agents which\n                implement the Cisco Circuit Interface MIB.')
ciscoCircuitInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 160, 3, 2, 1)).setObjects(("CISCO-CIRCUIT-INTERFACE-MIB", "cciDescr"), ("CISCO-CIRCUIT-INTERFACE-MIB", "cciStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCircuitInterfaceGroup = ciscoCircuitInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCircuitInterfaceGroup.setDescription('The Cisco Circuit Interface MIB objects.')
mibBuilder.exportSymbols("CISCO-CIRCUIT-INTERFACE-MIB", PYSNMP_MODULE_ID=ciscoCircuitInterfaceMIB, cciDescr=cciDescr, cciDescription=cciDescription, cciDescriptionEntry=cciDescriptionEntry, cciDescriptionTable=cciDescriptionTable, cciStatus=cciStatus, ciscoCircuitInterfaceGroup=ciscoCircuitInterfaceGroup, ciscoCircuitInterfaceMIB=ciscoCircuitInterfaceMIB, ciscoCircuitInterfaceMIBCompliance=ciscoCircuitInterfaceMIBCompliance, ciscoCircuitInterfaceMIBCompliances=ciscoCircuitInterfaceMIBCompliances, ciscoCircuitInterfaceMIBConformance=ciscoCircuitInterfaceMIBConformance, ciscoCircuitInterfaceMIBGroups=ciscoCircuitInterfaceMIBGroups, ciscoCircuitInterfaceMIBObjects=ciscoCircuitInterfaceMIBObjects)
