#
# PySNMP MIB module BEGEMOT-ATM-FREEBSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-ATM-FREEBSD-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:33:42 2022
# On host fv-az130-744 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
begemotAtmSysGroup, begemotAtmIfEntry = mibBuilder.importSymbols("BEGEMOT-ATM-MIB", "begemotAtmSysGroup", "begemotAtmIfEntry")
NgNodeIdOrZero, = mibBuilder.importSymbols("BEGEMOT-NETGRAPH-MIB", "NgNodeIdOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Unsigned32, MibIdentifier, TimeTicks, Counter64, NotificationType, IpAddress, ObjectIdentity, ModuleIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Unsigned32", "MibIdentifier", "TimeTicks", "Counter64", "NotificationType", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemotAtmFreeBSDGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1))
if mibBuilder.loadTexts: begemotAtmFreeBSDGroup.setLastUpdated('200408060000Z')
if mibBuilder.loadTexts: begemotAtmFreeBSDGroup.setOrganization('German Aerospace Centre')
if mibBuilder.loadTexts: begemotAtmFreeBSDGroup.setContactInfo('\t\tHartmut Brandt\n\n             Postal:    German Aerospace Centre (DLR)\n                        Institute of Communications and Navigation\n                        82234 Wessling\n                        Germany\n\n\t     Fax:\t+49 8153 28 2844\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: begemotAtmFreeBSDGroup.setDescription('The FreeBSD specific Begemot MIB for ATM interfaces.')
begemotAtmNgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1))
begemotAtmNgIfTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1, 1), )
if mibBuilder.loadTexts: begemotAtmNgIfTable.setStatus('current')
if mibBuilder.loadTexts: begemotAtmNgIfTable.setDescription('This table contains an entry for each hardware ATM\n\t    interface. The table is indexed by the interface index.')
begemotAtmNgIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1, 1, 1), )
begemotAtmIfEntry.registerAugmentions(("BEGEMOT-ATM-FREEBSD-MIB", "begemotAtmNgIfEntry"))
begemotAtmNgIfEntry.setIndexNames(*begemotAtmIfEntry.getIndexNames())
if mibBuilder.loadTexts: begemotAtmNgIfEntry.setStatus('current')
if mibBuilder.loadTexts: begemotAtmNgIfEntry.setDescription('This is a table entry describing one ATM hardware interface.')
begemotAtmNgIfNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1, 1, 1, 1), NgNodeIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmNgIfNodeId.setStatus('current')
if mibBuilder.loadTexts: begemotAtmNgIfNodeId.setDescription('The netgraph node id of the interface. If there is no\n\t    node corresponding to the interface, this is 0.')
mibBuilder.exportSymbols("BEGEMOT-ATM-FREEBSD-MIB", begemotAtmNgGroup=begemotAtmNgGroup, begemotAtmFreeBSDGroup=begemotAtmFreeBSDGroup, begemotAtmNgIfTable=begemotAtmNgIfTable, begemotAtmNgIfEntry=begemotAtmNgIfEntry, begemotAtmNgIfNodeId=begemotAtmNgIfNodeId, PYSNMP_MODULE_ID=begemotAtmFreeBSDGroup)
