#
# PySNMP MIB module RADLAN-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-LLDP-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 10:44:09 2023
# On host fv-az988-178 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
TruthValue, = mibBuilder.importSymbols("RADLAN-SNMPv2", "TruthValue")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, Counter64, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, NotificationType, MibIdentifier, Counter32, Gauge32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Counter64", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "NotificationType", "MibIdentifier", "Counter32", "Gauge32", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlLldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 110))
rlLldp.setRevisions(('2005-06-20 00:00',))
if mibBuilder.loadTexts: rlLldp.setLastUpdated('200506200000Z')
if mibBuilder.loadTexts: rlLldp.setOrganization('Radlan Computer Communications Ltd.')
rlLldpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 110, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpEnabled.setStatus('current')
mibBuilder.exportSymbols("RADLAN-LLDP-MIB", PYSNMP_MODULE_ID=rlLldp, rlLldpEnabled=rlLldpEnabled, rlLldp=rlLldp)
