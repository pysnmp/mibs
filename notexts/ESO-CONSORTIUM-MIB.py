#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 09:19:25 2024
# On host fv-az735-465 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, snmpModules, TimeTicks, NotificationType, IpAddress, iso, Gauge32, Unsigned32, enterprises, Bits, Counter64, ObjectIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "snmpModules", "TimeTicks", "NotificationType", "IpAddress", "iso", "Gauge32", "Unsigned32", "enterprises", "Bits", "Counter64", "ObjectIdentity", "MibIdentifier", "Counter32")
DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType")
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
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", esoConsortiumMIB=esoConsortiumMIB, usm3DESPrivProtocol=usm3DESPrivProtocol, PYSNMP_MODULE_ID=esoConsortiumMIB, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol, usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities)
