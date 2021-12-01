#
# PySNMP MIB module SUPERMICRO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/supermicro/SUPERMICRO-SMI
# Produced by pysmi-1.1.3 at Wed Dec  1 17:34:53 2021
# On host fv-az135-680 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Unsigned32, TimeTicks, ObjectIdentity, Gauge32, MibIdentifier, enterprises, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Unsigned32", "TimeTicks", "ObjectIdentity", "Gauge32", "MibIdentifier", "enterprises", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SUPERMICRO-SMI", supermicro=supermicro, smProducts=smProducts, PYSNMP_MODULE_ID=supermicro, smSSMInfo=smSSMInfo, smHealth=smHealth)
