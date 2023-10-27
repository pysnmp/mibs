#
# PySNMP MIB module ARRIS-CM-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-CM-DEVICE-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 12:05:23 2023
# On host fv-az642-142 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, iso, Counter64, ObjectIdentity, IpAddress, Integer32, TimeTicks, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "TimeTicks", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
arrisCmDevMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1))
arrisCmDevMib.setRevisions(('1902-11-08 00:00', '1902-10-29 00:00', '1902-10-23 00:00', '1902-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arrisCmDevMib.setRevisionsDescriptions(("Added object 'arrisCmDevEnableDocsis20'.", "Added object 'arrisCmDevProvMethodIndicator'.", "Added objects 'arrisCmDevSwImageName' and 'arrisCmDevSwImageBuildTime'.", 'Initial version',))
if mibBuilder.loadTexts: arrisCmDevMib.setLastUpdated('0212100000Z')
if mibBuilder.loadTexts: arrisCmDevMib.setOrganization('ARRIS Broadband')
if mibBuilder.loadTexts: arrisCmDevMib.setContactInfo('Robert Coley\n                      Postal: ARRIS Broadband\n                      3871 Lakefield Drive\n                      Suite 300\n                      Suwanee, GA 30024-1242\n                      U.S.A.\n                      Phone:  +1 770-622-8400\n                      E-mail: robert.coley@arrisi.com')
if mibBuilder.loadTexts: arrisCmDevMib.setDescription('This MIB module supplies the basic proprietary (ARRIS-specific)\n        management objects for ARRIS Cable Modem (CM) devices.')
class ArrsCmDevProvMethod(TextualConvention, Integer32):
    description = 'These are the various provisioning methods that are \n                 supported by the device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("docsisOnly", 0), ("fullPacketCable", 1), ("packetCableMinusKDC", 2), ("cps", 3), ("gupi", 4), ("singleMAC", 5))

arrisCmDevMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1))
arrisCmDevBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1))
arrisCmDevCmSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2))
arrisCmDevCmTest = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 3))
arrisCmDevPermanentSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 2))
arrisCmDevOperationalSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 3))
arrisCmDevSalesSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 4))
arrisCmDevManufacturingTest = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 3, 2))
arrisCmDevOperationalTest = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 3, 3))
arrisCmDevWanIsolationState = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off-InActiveMode", 1), ("on-ActiveMode", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisCmDevWanIsolationState.setStatus('current')
if mibBuilder.loadTexts: arrisCmDevWanIsolationState.setDescription("The object controls the state of WAN Isolation.  The meaning of \n          the state is as follows:\n          \n          off-InActiveMode(1) - Data traffic passes freely between \n             the home users network and the outside network (i.e. the Internet).  \n             In this mode, the WAN Isolation state is considered 'InActive'.\n\n          on-ActiveMode(2) - The home users network is isolated from the Internet.  \n             Data traffic will not pass between the home user's network and the Internet.  \n             In this mode, the WAN Isolation state is considered 'Active'.")
arrisCmDevSwImageName = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arrisCmDevSwImageName.setStatus('current')
if mibBuilder.loadTexts: arrisCmDevSwImageName.setDescription('The name of the software image currently operating on this device.')
arrisCmDevSwImageBuildTime = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arrisCmDevSwImageBuildTime.setStatus('current')
if mibBuilder.loadTexts: arrisCmDevSwImageBuildTime.setDescription('The build date and time of the software image currently operating on \n          this device.')
arrisCmDevProvMethodIndicator = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 3, 2), ArrsCmDevProvMethod()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisCmDevProvMethodIndicator.setStatus('current')
if mibBuilder.loadTexts: arrisCmDevProvMethodIndicator.setDescription("Indicates the method used to provision the device.  This object should only be \n          changed by the configuration file.  The following provisioning methods are supported:\n          \n             docsisOnly(0)          - DOCSIS-only provisioning\n                                    \n             fullPacketCable(1)     - fully PacketCable compliant provisioning\n             \n             packetCableMinusKDC(2) - same as 'fullPacketCable', except with IPSEC and \n                                      SNMPv3 disabled                                \n                                      \n             cps(3)                 - compatible with CPS2000 (SNMPv2; IPSEC disabled)\n             \n             gupi(4)                - SNMPv2, with no SNMP Informs and IPSEC disabled\n             \n             singleMAC(5)           - single config file (SNMPv2, single IP address, \n                                      single MAC address, no SNMP Informs, IPSEC disabled)")
arrisCmDevEnableDocsis20 = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 3, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisCmDevEnableDocsis20.setStatus('current')
if mibBuilder.loadTexts: arrisCmDevEnableDocsis20.setDescription('This object is used to enable/disable DOCSIS 2.0 operation mode.  \n           This object is stored into NVRAM and will be operational after \n           the next reboot of the device.\n           Set to true(1) to enable DOCSIS 2.0 operation mode.\n           Set to false(2) to disable DOCSIS 2.0 operation mode.  \n           Setting this object to the same value that is already stored in NVRAM \n           will do nothing.  After the successful setting of this object, the device \n           will automatically reboot.')
mibBuilder.exportSymbols("ARRIS-CM-DEVICE-MIB", PYSNMP_MODULE_ID=arrisCmDevMib, arrisCmDevManufacturingTest=arrisCmDevManufacturingTest, arrisCmDevMib=arrisCmDevMib, arrisCmDevPermanentSetup=arrisCmDevPermanentSetup, arrisCmDevProvMethodIndicator=arrisCmDevProvMethodIndicator, arrisCmDevEnableDocsis20=arrisCmDevEnableDocsis20, arrisCmDevCmSetup=arrisCmDevCmSetup, ArrsCmDevProvMethod=ArrsCmDevProvMethod, arrisCmDevCmTest=arrisCmDevCmTest, arrisCmDevBase=arrisCmDevBase, arrisCmDevWanIsolationState=arrisCmDevWanIsolationState, arrisCmDevMibObjects=arrisCmDevMibObjects, arrisCmDevOperationalSetup=arrisCmDevOperationalSetup, arrisCmDevSalesSetup=arrisCmDevSalesSetup, arrisCmDevOperationalTest=arrisCmDevOperationalTest, arrisCmDevSwImageName=arrisCmDevSwImageName, arrisCmDevSwImageBuildTime=arrisCmDevSwImageBuildTime)
