#
# PySNMP MIB module RAPID-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-INFO-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Wed May 29 02:47:15 2024
# On host fv-az569-426 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, enterprises, ModuleIdentity, iso, TimeTicks, Counter32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Gauge32, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "enterprises", "ModuleIdentity", "iso", "TimeTicks", "Counter32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Gauge32", "Integer32", "Unsigned32")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2001-04-20 12:00', '2002-11-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsInfoModule.setRevisionsDescriptions(('Initial revision.', 'Changed CONTACT-INFO.',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0103061200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: rsInfoModule.setContactInfo('   Ella Yu\n                      WatchGuard Technologies, Inc.\n                      1841 Zanker Road\n                      San Jose, CA 95112\n                      USA\n\n                      408-519-4888\n                      ella.yu@watchguard.com ')
if mibBuilder.loadTexts: rsInfoModule.setDescription('The MIB module describes general information\n            of RapidStream system.  Mainly, the information \n            obtained from this MIB is used by rsInfoSystemMIB,\n            rsClientMIB, rsSystemStatisticsMIB, rsIpsecTunnelMIB.')
rsInfoSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 1))
if mibBuilder.loadTexts: rsInfoSystem.setStatus('current')
if mibBuilder.loadTexts: rsInfoSystem.setDescription('This is the base system information for all rs Client\n             branches.')
rsInfoSystemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsInfoSystemCurrentTime.setStatus('current')
if mibBuilder.loadTexts: rsInfoSystemCurrentTime.setDescription("The host's notion of the local date and time of day.")
mibBuilder.exportSymbols("RAPID-INFO-SYSTEM-MIB", rsInfoSystemCurrentTime=rsInfoSystemCurrentTime, PYSNMP_MODULE_ID=rsInfoModule, rsInfoModule=rsInfoModule, rsInfoSystem=rsInfoSystem)
