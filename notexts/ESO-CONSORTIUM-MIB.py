#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 12:29:15 2023
# On host fv-az583-292 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Counter32, Bits, enterprises, Counter64, Integer32, NotificationType, Gauge32, ObjectIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter32", "Bits", "enterprises", "Counter64", "Integer32", "NotificationType", "Gauge32", "ObjectIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "MibIdentifier", "iso")
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
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", PYSNMP_MODULE_ID=esoConsortiumMIB, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol, esoConsortiumMIB=esoConsortiumMIB, usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, usm3DESPrivProtocol=usm3DESPrivProtocol, usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol)
