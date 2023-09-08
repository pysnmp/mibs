#
# PySNMP MIB module RAPID-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-INFO-SYSTEM-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 07:44:30 2023
# On host fv-az268-298 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, Gauge32, Integer32, ObjectIdentity, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Counter32, IpAddress, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Gauge32", "Integer32", "ObjectIdentity", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Counter32", "IpAddress", "TimeTicks", "Unsigned32", "iso")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
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
mibBuilder.exportSymbols("RAPID-INFO-SYSTEM-MIB", rsInfoSystem=rsInfoSystem, rsInfoSystemCurrentTime=rsInfoSystemCurrentTime, rsInfoModule=rsInfoModule, PYSNMP_MODULE_ID=rsInfoModule)
