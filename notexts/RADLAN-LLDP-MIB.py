#
# PySNMP MIB module RADLAN-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-LLDP-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 15:50:48 2022
# On host fv-az135-436 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
TruthValue, = mibBuilder.importSymbols("RADLAN-SNMPv2", "TruthValue")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Counter64, ObjectIdentity, Unsigned32, MibIdentifier, Integer32, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Counter64", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Integer32", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlLldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 110))
rlLldp.setRevisions(('2005-06-20 00:00',))
if mibBuilder.loadTexts: rlLldp.setLastUpdated('200506200000Z')
if mibBuilder.loadTexts: rlLldp.setOrganization('Radlan Computer Communications Ltd.')
rlLldpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 110, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpEnabled.setStatus('current')
mibBuilder.exportSymbols("RADLAN-LLDP-MIB", rlLldp=rlLldp, rlLldpEnabled=rlLldpEnabled, PYSNMP_MODULE_ID=rlLldp)
