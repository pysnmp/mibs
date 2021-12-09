#
# PySNMP MIB module SUPERMICRO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/supermicro/SUPERMICRO-SMI
# Produced by pysmi-1.1.3 at Thu Dec  9 15:35:42 2021
# On host fv-az83-649 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, Counter64, Integer32, NotificationType, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Counter32, ObjectIdentity, iso, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter64", "Integer32", "NotificationType", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Counter32", "ObjectIdentity", "iso", "enterprises", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
supermicro = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876))
supermicro.setRevisions(('2001-10-26 00:00',))
if mibBuilder.loadTexts: supermicro.setLastUpdated('200110260000Z')
if mibBuilder.loadTexts: supermicro.setOrganization('Super Micro Computer Inc.')
smProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 10876, 1))
if mibBuilder.loadTexts: smProducts.setStatus('current')
smHealth = ObjectIdentity((1, 3, 6, 1, 4, 1, 10876, 2))
if mibBuilder.loadTexts: smHealth.setStatus('current')
smSSMInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 10876, 100))
if mibBuilder.loadTexts: smSSMInfo.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-SMI", smSSMInfo=smSSMInfo, smHealth=smHealth, PYSNMP_MODULE_ID=supermicro, smProducts=smProducts, supermicro=supermicro)
