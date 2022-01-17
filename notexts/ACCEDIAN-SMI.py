#
# PySNMP MIB module ACCEDIAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACCEDIAN-SMI
# Produced by pysmi-1.1.8 at Mon Jan 17 21:59:16 2022
# On host fv-az77-149 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, Bits, Unsigned32, MibIdentifier, Integer32, Counter32, iso, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, NotificationType, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Bits", "Unsigned32", "MibIdentifier", "Integer32", "Counter32", "iso", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "NotificationType", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
accedianMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420))
accedianMIB.setRevisions(('2006-08-06 01:00',))
if mibBuilder.loadTexts: accedianMIB.setLastUpdated('200608060100Z')
if mibBuilder.loadTexts: accedianMIB.setOrganization('Accedian Networks, Inc.')
acdProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 1))
if mibBuilder.loadTexts: acdProducts.setStatus('current')
acdMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 2))
if mibBuilder.loadTexts: acdMibs.setStatus('current')
acdTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 3))
if mibBuilder.loadTexts: acdTraps.setStatus('current')
acdExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 4))
acdServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 22420, 5))
if mibBuilder.loadTexts: acdServices.setStatus('current')
mibBuilder.exportSymbols("ACCEDIAN-SMI", acdProducts=acdProducts, acdExperiment=acdExperiment, acdMibs=acdMibs, PYSNMP_MODULE_ID=accedianMIB, acdServices=acdServices, acdTraps=acdTraps, accedianMIB=accedianMIB)
