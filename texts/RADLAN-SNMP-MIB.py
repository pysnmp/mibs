#
# PySNMP MIB module RADLAN-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SNMP-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:27:23 2024
# On host fv-az1019-803 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, MibIdentifier, ObjectIdentity, Integer32, Counter32, ModuleIdentity, NotificationType, IpAddress, TimeTicks, Bits, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Integer32", "Counter32", "ModuleIdentity", "NotificationType", "IpAddress", "TimeTicks", "Bits", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlSNMP = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 98))
rlSNMP.setRevisions(('1904-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSNMP.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlSNMP.setLastUpdated('0410200000Z')
if mibBuilder.loadTexts: rlSNMP.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlSNMP.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlSNMP.setDescription('Private MIB module for SNMP support in Radlan devices.')
rlSNMPv3 = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 98, 1))
rlTargetParamsTestingLevel = MibScalar((1, 3, 6, 1, 4, 1, 89, 98, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTargetParamsTestingLevel.setStatus('current')
if mibBuilder.loadTexts: rlTargetParamsTestingLevel.setDescription('The level of the tests done when configuring an entry in the snmpTargetParamsTable.')
rlNotifyFilterTestingLevel = MibScalar((1, 3, 6, 1, 4, 1, 89, 98, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlNotifyFilterTestingLevel.setStatus('current')
if mibBuilder.loadTexts: rlNotifyFilterTestingLevel.setDescription('The level of the tests done when configuring an entry in the snmpNotifyFilterTable.')
rlSnmpEngineID = MibScalar((1, 3, 6, 1, 4, 1, 89, 98, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 32)).clone(hexValue="0000000001")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnmpEngineID.setStatus('current')
if mibBuilder.loadTexts: rlSnmpEngineID.setDescription("A variable for setting the router's local engineID value.\n         Setting this variable will effect the value of snmpEngineID. Setting this\n         variable to the value '00 00 00 00 00'H will cause snmpEngineID to get\n         an automatically created value based on the device basic MAC address.\n         This method of setting the agent's engineID is recommended for stand-alone\n         systems. Setting this variable to any other (valid) value will set snmpEngineID\n         to this value. Setting this variable to all 'ff'H or all zeros is not\n         allowed, with the exception of the value '00 00 00 00 00'H.\n         The last method is recommended for stackable system, in order for the\n         engineID to be unique within an administrative domain.\n         Setting this value (to a value different then the default value)\n         is required before configuring the usmUserTable.\n         Changing the value of this variable has 2 side-effects:\n         - All usmUserTable configured entries will be deleted.\n         - All snmpCommunityTable entries with snmpCommunityContextEngineID value\n           equal to old rlSnmpEngineID value, will be updated with the new\n           rlSnmpEngineID value.")
rlSNMPDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 98, 2))
rlSnmpUDPMridDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 89, 98, 2, 1))
if mibBuilder.loadTexts: rlSnmpUDPMridDomain.setStatus('current')
if mibBuilder.loadTexts: rlSnmpUDPMridDomain.setDescription('The SNMPv2 over UDP transport domain, used when Multi-Instance Router\n             is supported (more than one MIR instance exist).\n             The corresponding transport address is of type RlSnmpUDPMridAddress.')
class RlSnmpUDPMridAddress(TextualConvention, OctetString):
    description = 'Represents the UDP address of NMS and the MRID through which it is\n             connected in order to access the agent:\n               octets   contents        encoding\n                1-4     IP-address      network-byte order\n                5-6     UDP-port        network-byte order\n                7-8     MRID            network-byte order\n            '
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d/2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

rlSnmpRequestMridTable = MibTable((1, 3, 6, 1, 4, 1, 89, 98, 3), )
if mibBuilder.loadTexts: rlSnmpRequestMridTable.setStatus('current')
if mibBuilder.loadTexts: rlSnmpRequestMridTable.setDescription('A table for determining the Mrid for the current SNMP request.')
rlSnmpRequestMridEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 98, 3, 1), ).setIndexNames((0, "RADLAN-SNMP-MIB", "rlSnmpRequestManagedMrid"))
if mibBuilder.loadTexts: rlSnmpRequestMridEntry.setStatus('current')
if mibBuilder.loadTexts: rlSnmpRequestMridEntry.setDescription(' The row definition for this table.')
rlSnmpRequestManagedMrid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpRequestManagedMrid.setStatus('current')
if mibBuilder.loadTexts: rlSnmpRequestManagedMrid.setDescription('The router instance the NMS wants to manage in the current SNMP request.\n     The value of this object, when attaching a variable instance of the\n     rlSnmpRequestManagedMridTable to an SNMP request, will determine the\n     managed Mrid for this request.\n     It is important to mention that the variable insance must be attached\n     as the first variable in the PDU in order to influence all variables.')
rlSnmpRequestMridStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnmpRequestMridStatus.setStatus('current')
if mibBuilder.loadTexts: rlSnmpRequestMridStatus.setDescription('The status of this entry.')
mibBuilder.exportSymbols("RADLAN-SNMP-MIB", rlSNMPDomains=rlSNMPDomains, rlSnmpRequestManagedMrid=rlSnmpRequestManagedMrid, rlSnmpUDPMridDomain=rlSnmpUDPMridDomain, rlSnmpRequestMridTable=rlSnmpRequestMridTable, RlSnmpUDPMridAddress=RlSnmpUDPMridAddress, rlTargetParamsTestingLevel=rlTargetParamsTestingLevel, rlNotifyFilterTestingLevel=rlNotifyFilterTestingLevel, rlSnmpRequestMridEntry=rlSnmpRequestMridEntry, rlSNMP=rlSNMP, PYSNMP_MODULE_ID=rlSNMP, rlSNMPv3=rlSNMPv3, rlSnmpEngineID=rlSnmpEngineID, rlSnmpRequestMridStatus=rlSnmpRequestMridStatus)
