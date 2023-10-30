#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.10 at Mon Oct 30 02:17:56 2023
# On host fv-az879-766 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, Bits, Integer32, enterprises, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, MibIdentifier, IpAddress, Counter64, Unsigned32, TimeTicks, Counter32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Bits", "Integer32", "enterprises", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "MibIdentifier", "IpAddress", "Counter64", "Unsigned32", "TimeTicks", "Counter32", "NotificationType", "ModuleIdentity")
AutonomousType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", usm3DESPrivProtocol=usm3DESPrivProtocol, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities, usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol, PYSNMP_MODULE_ID=esoConsortiumMIB, esoConsortiumMIB=esoConsortiumMIB, usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol)
