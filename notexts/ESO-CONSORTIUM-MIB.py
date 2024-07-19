#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:01:55 2024
# On host fv-az1251-884 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter32, Unsigned32, NotificationType, ModuleIdentity, snmpModules, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, IpAddress, TimeTicks, MibIdentifier, Counter64, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Unsigned32", "NotificationType", "ModuleIdentity", "snmpModules", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "IpAddress", "TimeTicks", "MibIdentifier", "Counter64", "Bits", "Gauge32")
AutonomousType, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DisplayString", "TextualConvention")
esoConsortiumMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14832))
esoConsortiumMIB.setRevisions(('2004-06-23 00:00', '2003-02-03 00:00', '2003-02-03 00:00',))
if mibBuilder.loadTexts: esoConsortiumMIB.setLastUpdated('200406230000Z')
if mibBuilder.loadTexts: esoConsortiumMIB.setOrganization('ESO (Extended Security Options) Consortium')
esoConsortiumMIBObjectIdentities = MibIdentifier((1, 3, 6, 1, 4, 1, 14832, 1))
usm3DESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 1))
if mibBuilder.loadTexts: usm3DESPrivProtocol.setStatus('current')
usmAESCfb128PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 2))
if mibBuilder.loadTexts: usmAESCfb128PrivProtocol.setStatus('deprecated')
usmAESCfb192PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 3))
if mibBuilder.loadTexts: usmAESCfb192PrivProtocol.setStatus('current')
usmAESCfb256PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 4))
if mibBuilder.loadTexts: usmAESCfb256PrivProtocol.setStatus('current')
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", usm3DESPrivProtocol=usm3DESPrivProtocol, PYSNMP_MODULE_ID=esoConsortiumMIB, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities, usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol, esoConsortiumMIB=esoConsortiumMIB, usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol)
